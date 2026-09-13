"""Resonance and Q-factor extraction for a 2D photonic-crystal cavity.

The plotting parameters intentionally follow the original script/notebook so
that regenerated geometry figures remain consistent with ``docs/images``.
"""

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import meep as mp
import numpy as np

from geometry import LineDefectCavity


plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 15
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "fig"
OUT_DIR = SCRIPT_DIR / "out"
FIG_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)


@dataclass(frozen=True)
class SimulationConfig:
    nx: int = 8
    ny: int = 30
    cavity_length: int = 5
    end_hole_shift: float = 0.2
    hole_radius: float = 0.25
    effective_index: float = 2.6
    center_frequency: float = 0.25
    frequency_width: float = 0.05
    resolution: int = 16
    pml_thickness: float = 1.0
    cell_buffer: float = 4.0
    run_time_after_source: float = 3000.0


def build_simulation(config: SimulationConfig) -> mp.Simulation:
    """Construct the 2D line-defect cavity simulation."""
    cell = mp.Vector3(
        config.ny + config.cell_buffer,
        (config.nx + config.cell_buffer / 2) * np.sqrt(3),
        0,
    )

    dielectric = mp.Medium(epsilon=config.effective_index**2)
    background = mp.Block(size=mp.Vector3(mp.inf, mp.inf, mp.inf), material=dielectric)

    cavity = LineDefectCavity(
        nx=config.nx,
        ny=config.ny,
        cavity_length=config.cavity_length,
        end_hole_shift=config.end_hole_shift,
        hole_radius=config.hole_radius,
    )

    sources = [
        mp.Source(
            mp.GaussianSource(config.center_frequency, fwidth=config.frequency_width),
            component=mp.Hz,
            center=mp.Vector3(0.5, 0),
            amplitude=1,
        ),
        mp.Source(
            mp.GaussianSource(config.center_frequency, fwidth=config.frequency_width),
            component=mp.Hz,
            center=mp.Vector3(-0.5, 0),
            amplitude=-1,
        ),
    ]

    return mp.Simulation(
        cell_size=cell,
        geometry=[background, *cavity.to_meep()],
        boundary_layers=[mp.PML(config.pml_thickness)],
        sources=sources,
        symmetries=[mp.Mirror(mp.Y, phase=-1)],
        resolution=config.resolution,
    )


def save_modes(modes: list) -> None:
    """Write the Harminv resonance table to CSV."""
    rows = np.array([[mode.freq, mode.q] for mode in modes], dtype=float)
    if rows.size == 0:
        rows = np.empty((0, 2), dtype=float)

    np.savetxt(
        OUT_DIR / "harminv_modes.csv",
        rows,
        delimiter=",",
        header="normalized_frequency,Q",
        comments="",
    )


def main() -> None:
    config = SimulationConfig()
    simulation = build_simulation(config)

    fig = plt.figure(dpi=100)
    simulation.plot2D(ax=fig.gca())
    fig.savefig(FIG_DIR / "harminv_cavity_geometry.png")
    plt.show()

    harminv = mp.Harminv(
        mp.Hz,
        mp.Vector3(),
        config.center_frequency,
        config.frequency_width,
    )
    simulation.run(
        mp.after_sources(harminv),
        until_after_sources=config.run_time_after_source,
    )

    save_modes(harminv.modes)

    if not harminv.modes:
        print("No resonances were found in the requested frequency window.")
        return

    print("Detected cavity modes:")
    for mode in harminv.modes:
        print(f"  f = {mode.freq:.8f}, Q = {mode.q:.3g}")


if __name__ == "__main__":
    main()
