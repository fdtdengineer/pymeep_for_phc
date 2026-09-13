"""Band structure of a 2D triangular-lattice photonic crystal.

The unit cell is a dielectric background with one circular air hole. MPB is
used to compute TE and TM bands along the high-symmetry path Gamma-K-M-Gamma.
All lengths are normalized by the lattice constant ``a``.

The plotting parameters intentionally follow the original notebook so that
newly generated figures remain visually consistent with ``docs/images``.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import meep as mp
from meep import mpb
import numpy as np


N_BACKGROUND = 2.6
HOLE_RADIUS = 0.25
NUM_BANDS = 4
RESOLUTION = 32
POINTS_PER_SEGMENT = 10

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
FIG_DIR.mkdir(exist_ok=True)


def build_solver() -> mpb.ModeSolver:
    """Create an MPB solver for a triangular lattice with a circular air hole."""
    lattice = mp.Lattice(
        size=mp.Vector3(1, 1),
        basis1=mp.Vector3(0.5, np.sqrt(3) / 2),
        basis2=mp.Vector3(0.5, -np.sqrt(3) / 2),
    )

    geometry = [
        mp.Block(
            material=mp.Medium(epsilon=N_BACKGROUND**2),
            size=mp.Vector3(mp.inf, mp.inf),
        ),
        mp.Cylinder(
            radius=HOLE_RADIUS,
            material=mp.Medium(epsilon=1.0),
        ),
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
        k_points=k_points,
        resolution=RESOLUTION,
        num_bands=NUM_BANDS,
    )


def plot_geometry(mode_solver: mpb.ModeSolver) -> None:
    """Plot three periods of the dielectric function using the original style."""
    converter = mpb.MPBData(rectify=True, periods=3, resolution=64)
    epsilon = converter.convert(mode_solver.get_epsilon())

    fig = plt.figure()
    plt.imshow(epsilon, interpolation="spline36", cmap="binary")
    plt.axis("off")
    fig.savefig(FIG_DIR / "geometry.png")
    plt.show()


def plot_bands(te_freqs: np.ndarray, te_gaps: list) -> None:
    """Plot the TE bands using the same settings as the original notebook."""
    fig, ax = plt.subplots(figsize=(4.8, 4))
    x = range(len(te_freqs))

    ax.plot(te_freqs, color="black")
    ax.set_ylim([te_freqs.min(), te_freqs.max()])
    ax.set_xlim([x[0], x[-1]])

    for gap in te_gaps:
        if gap[0] > 1:
            ax.fill_between(x, gap[1], gap[2], color="black", alpha=0.2)

    ax.text(12, 0.04, "TE bands", color="black", size=FS)

    points_in_between = (len(te_freqs) - 4) / 3
    tick_locs = [i * points_in_between + i for i in range(4)]
    tick_labs = ["Γ", "K", "M", "Γ"]
    ax.set_xticks(tick_locs)
    ax.set_xticklabels(tick_labs, size=FS)
    ax.set_ylabel("Frequency (c/a)", size=FS)
    plt.tick_params(labelsize=FS)

    fig.savefig(FIG_DIR / "band_structure.png")
    plt.show()


def main() -> None:
    solver = build_solver()

    solver.run_tm()
    tm_freqs = np.array(solver.all_freqs, copy=True)
    tm_gaps = list(solver.gap_list)
    _ = (tm_freqs, tm_gaps)  # Retained for interactive comparison with the notebook.

    solver.run_te()
    te_freqs = np.array(solver.all_freqs, copy=True)
    te_gaps = list(solver.gap_list)

    plot_geometry(solver)
    plot_bands(te_freqs, te_gaps)


if __name__ == "__main__":
    main()
