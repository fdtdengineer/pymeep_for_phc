"""Geometry helpers for line-defect photonic-crystal cavities."""

from dataclasses import dataclass

import meep as mp
import numpy as np


@dataclass(frozen=True)
class LineDefectCavity:
    """Triangular-lattice cavity formed by removing holes from one lattice row.

    Parameters are expressed in units of the lattice constant ``a``. The
    geometry is generated in a triangular lattice and then rotated by 90 degrees
    so that the cavity axis lies along the x direction used by the Meep examples.
    """

    a: float = 1.0
    nx: int = 8
    ny: int = 30
    cavity_length: int = 5
    end_hole_shift: float = 0.2
    hole_radius: float = 0.25
    offset_x: float = 0.0
    offset_y: float = 0.0

    def hole_centers(self) -> np.ndarray:
        """Return the air-hole centers as an ``(N, 2)`` array."""
        dx = self.a * np.sqrt(3) / 2
        dy = self.a
        x0 = self.offset_x - self.nx * dx
        y0 = self.offset_y - self.ny * dy / 2
        centers: list[tuple[float, float]] = []

        for j in range(self.nx + 1):
            for i in range(self.ny + 1):
                on_cavity_row = 2 * j == self.nx
                cavity_coordinate = 2 * i - self.ny

                if on_cavity_row and abs(cavity_coordinate) <= self.cavity_length - 1:
                    continue

                y = y0 + dy * i
                if on_cavity_row and abs(cavity_coordinate) == self.cavity_length + 1:
                    y += self.end_hole_shift * self.a * np.sign(cavity_coordinate)

                x = x0 + 2 * dx * j
                centers.append((x, y))

        for j in range(self.nx):
            for i in range(self.ny):
                x = x0 + dx + 2 * dx * j
                y = y0 + dy / 2 + dy * i
                centers.append((x, y))

        points = np.asarray(centers, dtype=float)
        return np.column_stack((points[:, 1], -points[:, 0]))

    def to_meep(self) -> list:
        """Convert the hole centers into Meep air cylinders."""
        return [
            mp.Cylinder(
                radius=self.hole_radius,
                center=mp.Vector3(x, y),
                material=mp.air,
            )
            for x, y in self.hole_centers()
        ]
