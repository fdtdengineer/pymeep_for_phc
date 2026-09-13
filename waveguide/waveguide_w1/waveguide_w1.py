"""Transmission spectrum of a 2D W1 photonic-crystal waveguide.

A triangular lattice of air holes is etched into an effective-index dielectric.
The output flux is normalized by a straight-waveguide reference simulation.
Plotting settings intentionally follow the original notebook so that regenerated
figures remain visually consistent with ``docs/images``.
"""

from dataclasses import dataclass, replace
from pathlib import Path
import time

import matplotlib.pyplot as plt
import meep as mp
import numpy as np


FS = 18
plt.rcParams.update(
    {
        "font.family": "Arial",
        "font.sans-serif": ["Arial"],
        "font.size": FS,
        "xtick.direction": "in",
        "ytick.direction": "in",
    }
)

SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "fig"
OUT_DIR = SCRIPT_DIR / "out"
FIG_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)


@dataclass(frozen=True)
class SimulationConfig:
    """Numerical and geometric parameters in units of the lattice constant."""

    phc_length: int = 40
    phc_width: int = 10
    connection_length: float = 5.0
    waveguide_width: float = 1.0
    hole_radius: float = 0.25
    effective_index: float = 2.6
    center_frequency: float = 0.30
    frequency_width: float = 0.10
    num_frequencies: int = 500
    resolution: int = 16
    pml_thickness: float = 1.0
    decay_threshold: float = 1e-7


@dataclass(frozen=True)
class Spectrum:
    frequencies: np.ndarray
    flux: np.ndarray


def build_geometry(config: SimulationConfig, use_photonic_crystal: bool) -> tuple[mp.Vector3, list]:
    """Build the simulation cell and geometry for the reference or W1 device."""
    length = config.phc_length + 2 * config.connection_length
    width = config.phc_width * np.sqrt(3)
    epsilon = config.effective_index**2

    cell = mp.Vector3(length, width, 0)
    material = mp.Medium(epsilon=epsilon)

    geometry = [
        mp.Block(
            size=mp.Vector3(mp.inf, config.waveguide_width * np.sqrt(3), mp.inf),
            material=material,
        )
    ]

    if not use_photonic_crystal:
        return cell, geometry

    geometry.append(
        mp.Block(
            size=mp.Vector3(config.phc_length, width, mp.inf),
            material=material,
        )
    )

    nx = int(config.phc_length)
    ny = int(config.phc_width)
    half_gap = config.waveguide_width * np.sqrt(3) / 2

    for row in range(ny):
        shift_y = np.sqrt(3)
        for col in range(nx + 1):
            x_a = col - nx / 2
            x_b = col - (nx + 1) / 2
            for x, y in (
                (x_a, half_gap + shift_y * row),
                (x_a, -(half_gap + shift_y * row)),
                (x_b, half_gap + shift_y * (row + 0.5)),
                (x_b, -(half_gap + shift_y * (row + 0.5))),
            ):
                geometry.append(
                    mp.Cylinder(
                        radius=config.hole_radius,
                        center=mp.Vector3(x, y),
                        material=mp.air,
                    )
                )

    return cell, geometry


def run_spectrum(
    config: SimulationConfig,
    use_photonic_crystal: bool,
    decay_check: float,
    plot_geometry: bool = False,
) -> Spectrum:
    """Run one Meep simulation and return its output-flux spectrum."""
    cell, geometry = build_geometry(config, use_photonic_crystal)
    length = cell.x

    sources = [
        mp.Source(
            mp.GaussianSource(config.center_frequency, fwidth=config.frequency_width),
            component=mp.Hz,
            center=mp.Vector3(-length / 2 + 1, 0),
            size=mp.Vector3(0, config.waveguide_width * np.sqrt(3)),
        )
    ]

    simulation = mp.Simulation(
        cell_size=cell,
        boundary_layers=[mp.PML(config.pml_thickness)],
        geometry=geometry,
        sources=sources,
        symmetries=[mp.Mirror(mp.Y, phase=-1)],
        resolution=config.resolution,
    )

    monitor_region = mp.FluxRegion(
        center=mp.Vector3(length / 2 - 1.5, 0),
        size=mp.Vector3(0, 2 * config.waveguide_width),
    )
    monitor = simulation.add_flux(
        config.center_frequency,
        config.frequency_width,
        config.num_frequencies,
        monitor_region,
    )

    if plot_geometry:
        fig = plt.figure(dpi=100)
        simulation.plot2D(ax=fig.gca())
        fig.savefig(FIG_DIR / "geometry_phc.png")
        plt.show()

    simulation.run(
        until_after_sources=mp.stop_when_fields_decayed(
            50,
            mp.Hz,
            mp.Vector3(decay_check),
            config.decay_threshold,
        )
    )

    frequencies = np.asarray(mp.get_flux_freqs(monitor), dtype=float)
    flux = np.asarray(mp.get_fluxes(monitor), dtype=float)
    simulation.reset_meep()
    return Spectrum(frequencies=frequencies, flux=flux)


def main() -> None:
    config = SimulationConfig()
    start = time.perf_counter()

    reference = run_spectrum(
        replace(config, phc_length=20),
        use_photonic_crystal=False,
        decay_check=10,
    )
    device = run_spectrum(
        replace(config, phc_length=40),
        use_photonic_crystal=True,
        decay_check=20,
        plot_geometry=True,
    )

    if not np.allclose(reference.frequencies, device.frequencies):
        raise RuntimeError("Reference and device frequency grids do not match.")

    transmittance = np.divide(
        device.flux,
        reference.flux,
        out=np.full_like(device.flux, np.nan),
        where=np.abs(reference.flux) > 1e-14,
    )

    lattice_constant_nm = 400.0
    wavelength_nm = lattice_constant_nm / device.frequencies
    data = np.column_stack((device.frequencies, wavelength_nm, transmittance))
    np.savetxt(
        OUT_DIR / "transmittance.csv",
        data,
        delimiter=",",
        header="normalized_frequency,wavelength_nm,transmittance",
        comments="",
    )

    plt.figure(figsize=(5.4, 4), dpi=100)
    plt.plot(wavelength_nm, transmittance, color="#0072bc")
    plt.scatter(wavelength_nm, transmittance, color="#0072bc")
    plt.xlabel("Frequency [c/a]")
    plt.ylabel("Transmittance [c/a]")
    plt.xlim([wavelength_nm[-1], wavelength_nm[0]])
    plt.yscale("log")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "phcwaveguide_transmittance1.png")
    plt.show()

    elapsed = time.perf_counter() - start
    print(f"Completed reference and W1 simulations in {elapsed:.1f} s")


if __name__ == "__main__":
    main()
