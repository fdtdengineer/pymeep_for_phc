"""Band structure of a 2D triangular-lattice photonic crystal.

The unit cell is a dielectric background with one circular air hole. MPB is
used to compute TE and TM bands along the high-symmetry path Gamma-K-M-Gamma.
All lengths are normalized by the lattice constant ``a``.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import meep as mp
from meep import mpb
import numpy as np


N_BACKGROUND = 2.6
HOLE_RADIUS = 0.25
NUM_BANDS = 6
RESOLUTION = 32
POINTS_PER_SEGMENT = 30

SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "fig"
FIG_DIR.mkdir(exist_ok=True)


def build_solver() -> mpb.ModeSolver:
    """Create an MPB solver for a triangular lattice with a circular air hole."""
    lattice = mp.Lattice(
        size=mp.Vector3(1, 1),
        basis1=mp.Vector3(0.5, np.sqrt(3) / 2),
        basis2=mp.Vector3(0.5, -np.sqrt(3) / 2),
    )

    geometry = [
        mp.Cylinder(
            radius=HOLE_RADIUS,
            material=mp.air,
        )
    ]

    high_symmetry_points = [
        mp.Vector3(),
        mp.Vector3(1 / 3, 1 / 3),
        mp.Vector3(1 / 2, 0),
        mp.Vector3(),
    ]
    k_points = mp.interpolate(POINTS_PER_SEGMENT, high_symmetry_points)

    return mpb.ModeSolver(
        geometry_lattice=lattice,
        geometry=geometry,
        default_material=mp.Medium(index=N_BACKGROUND),
        k_points=k_points,
        resolution=RESOLUTION,
        num_bands=NUM_BANDS,
    )


def plot_geometry(mode_solver: mpb.ModeSolver) -> None:
    """Plot three periods of the dielectric function."""
    converter = mpb.MPBData(rectify=True, periods=3, resolution=64)
    epsilon = converter.convert(mode_solver.get_epsilon())

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(epsilon.T, interpolation="nearest", cmap="binary")
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "geometry.png", dpi=180, bbox_inches="tight")
    plt.show()


def plot_bands(te_freqs: np.ndarray, tm_freqs: np.ndarray) -> None:
    """Plot TE and TM bands on the Gamma-K-M-Gamma path."""
    x = np.arange(te_freqs.shape[0])
    segment = POINTS_PER_SEGMENT + 1
    tick_locs = [0, segment, 2 * segment, 3 * segment]

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot(x, te_freqs, color="black", linewidth=1.5, label="TE")
    ax.plot(x, tm_freqs, color="#0072bc", linewidth=1.5, linestyle="--", label="TM")
    ax.set_xlim(x[0], x[-1])
    ax.set_xticks(tick_locs)
    ax.set_xticklabels([r"$\Gamma$", "K", "M", r"$\Gamma$"])
    ax.set_ylabel(r"Normalized frequency $\omega a / 2\pi c$")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "band_structure.png", dpi=180, bbox_inches="tight")
    plt.show()


def main() -> None:
    solver = build_solver()

    solver.run_te()
    te_freqs = np.array(solver.all_freqs, copy=True)

    solver.run_tm()
    tm_freqs = np.array(solver.all_freqs, copy=True)

    plot_geometry(solver)
    plot_bands(te_freqs, tm_freqs)


if __name__ == "__main__":
    main()
