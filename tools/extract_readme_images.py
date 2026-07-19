"""Extract selected embedded PNG outputs from notebooks for README.md.

This script does not rerun any simulation. It decodes the image/png payloads already
stored in the committed Jupyter notebooks, so the documentation figures are exact
copies of the notebook outputs.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "images"


def embedded_pngs(notebook_path: Path) -> list[bytes]:
    """Return all embedded PNG outputs in notebook cell order."""
    with notebook_path.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    images: list[bytes] = []
    for cell in notebook.get("cells", []):
        for output in cell.get("outputs", []):
            png = output.get("data", {}).get("image/png")
            if png is None:
                continue
            if isinstance(png, list):
                png = "".join(png)
            images.append(base64.b64decode(png))
    return images


def write_png(image: bytes, relative_path: str) -> None:
    destination = OUTPUT_DIR / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(image)
    print(f"wrote {destination.relative_to(ROOT)} ({len(image):,} bytes)")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    band_images = embedded_pngs(ROOT / "mpb_band" / "2D_hole_cir.ipynb")
    if len(band_images) < 2:
        raise RuntimeError("2D_hole_cir.ipynb does not contain the expected PNG outputs")
    write_png(band_images[0], "2d_hole_cir_geometry.png")
    write_png(band_images[-1], "2d_hole_cir_band_structure.png")

    cavity_images = embedded_pngs(ROOT / "cavity" / "eigenmode" / "harminv_cavity.ipynb")
    if not cavity_images:
        raise RuntimeError("harminv_cavity.ipynb does not contain an embedded geometry image")
    write_png(cavity_images[0], "harminv_cavity_geometry.png")

    waveguide_images = embedded_pngs(ROOT / "waveguide" / "waveguide_w1" / "waveguide_w1.ipynb")
    if len(waveguide_images) < 2:
        raise RuntimeError("waveguide_w1.ipynb does not contain the expected PNG outputs")

    # The notebook first plots the straight reference waveguide and then the PhC
    # waveguide. The final embedded PNG is the transmittance spectrum.
    geometry_index = 1 if len(waveguide_images) >= 3 else 0
    write_png(waveguide_images[geometry_index], "waveguide_w1_geometry.png")
    write_png(waveguide_images[-1], "waveguide_w1_transmittance.png")


if __name__ == "__main__":
    main()
