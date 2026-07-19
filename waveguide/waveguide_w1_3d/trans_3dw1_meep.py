#%%
# mpirun -np 8 python test/transmittance_3dw1wg/trans_3dw1_meep.py

"""
Standalone version of transmittance_3DW1waveguide.py with the PhC geometry
classes and the Meep parser inlined.

This removes the local-file dependencies:
    import geometry
    import parse_to_meep
    
It depends only on:
    numpy, pandas, meep, matplotlib
plus the Python standard library.
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
import meep as mp
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "fig"
OUT_DIR = SCRIPT_DIR / "out"
FIG_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)
fs = 18
plt.rcParams.update({
    'font.family': 'Liberation Sans',
    'font.sans-serif': ['Liberation Sans'],
    'font.size': fs,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
})


# -----------------------------------------------------------------------------
# Inlined from geometry.py
# -----------------------------------------------------------------------------
class GeometryPhC:
    """Base class for photonic-crystal hole-position generators."""

    dict_geometry_mp = {
        "circle": ["radius"],
    }

    def __init__(self):
        # Keep these instance-local.  The original code used class attributes,
        # which can leak geometry if multiple PhC objects are created.
        self.dict_kargs = {}
        self.dict_geometry = {}

    def get_geometry(self):
        return self.dict_geometry

    def get_kargs(self):
        return self.dict_kargs


class WidthModulated(GeometryPhC):
    def __init__(
        self,
        a,
        nx,
        ny,
        offset_x,
        offset_y,
        len_barrier,
        wgo,
        wgi,
        holeshift,
        radius=0.25,
    ):
        super().__init__()
        # a: lattice constant
        # nx, ny: number of holes in x and y directions
        # offset_x, offset_y: offset of the center of the unit cell
        # len_barrier: barrier length
        # wgo: outer waveguide width
        # wgi: internal waveguide width
        # holeshift: hole shift in both sides of holes of the cavity
        # radius: radius of holes for parser to meep
        self.a = a
        self.nx = nx
        self.ny = ny
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.len_barrier = len_barrier
        self.wgo = wgo
        self.wgi = wgi
        self.holeshift = holeshift
        self.radius = radius

        self.gen_geometry()

    def gen_geometry(self, holetype="circle", rotation=True):
        # holetype: "circle" as default
        # rotation: whether to apply 90 degree rotation to the geometry
        arr_lochole = []
        dx = self.a * np.sqrt(3) / 2
        dy = self.a
        dwgo = (self.wgo - 1) * self.a * np.sqrt(3)
        dwgi = (self.wgi - 1) * self.a * np.sqrt(3)
        x_center = self.offset_x - self.nx * dx
        y_center = self.offset_y - self.ny * dy / 2

        for j in range(self.nx + 1):
            for i in range(self.ny + 1):
                if 2 * j == self.nx:  # Center row is opened.
                    continue

                y = y_center + dy * i

                if abs(2 * j - self.nx) == 2 and abs(2 * i - self.ny) <= 2:
                    x = (
                        x_center
                        + 2 * dx * j
                        + dwgo * np.sign(2 * j - self.nx)
                        + 2 * self.holeshift * np.sign(2 * j - self.nx)
                    )
                elif abs(2 * j - self.nx) == 2 and abs(2 * i - self.ny) == 4:
                    x = (
                        x_center
                        + 2 * dx * j
                        + dwgo * np.sign(2 * j - self.nx)
                        + self.holeshift * np.sign(2 * j - self.nx)
                    )
                elif abs(2 * i - self.ny) <= 2 * self.len_barrier:
                    x = x_center + 2 * dx * j + dwgo * np.sign(2 * j - self.nx)
                else:
                    x = x_center + 2 * dx * j + dwgi * np.sign(2 * j - self.nx)

                arr_lochole.append([x, y])

        for j in range(self.nx):
            for i in range(self.ny):
                y = y_center + dy / 2 + dy * i
                signed_col = 2 * j - self.nx + 1
                col_sign = np.sign(signed_col)

                if abs(signed_col) == 1 and abs(2 * i - self.ny + 1) <= 1:
                    x = x_center + dx + 2 * dx * j + dwgo * col_sign + 3 * self.holeshift * col_sign
                elif abs(signed_col) == 1 and abs(2 * i - self.ny + 1) == 3:
                    x = x_center + dx + 2 * dx * j + dwgo * col_sign + 2 * self.holeshift * col_sign
                elif (abs(signed_col) == 3 and abs(2 * i - self.ny + 1) <= 3) or (
                    abs(signed_col) == 1 and abs(2 * i - self.ny + 1) == 5
                ):
                    x = x_center + dx + 2 * dx * j + dwgo * col_sign + self.holeshift * col_sign
                elif abs(2 * i - self.ny + 1) <= 2 * self.len_barrier:
                    x = x_center + dx + 2 * dx * j + dwgo * col_sign
                else:
                    x = x_center + dx + 2 * dx * j + dwgi * col_sign

                arr_lochole.append([x, y])

        npr_geometry = np.array(arr_lochole)

        if rotation:
            npr_geometry = np.array([npr_geometry[:, 1], -npr_geometry[:, 0]]).T

        self.dict_geometry[holetype] = npr_geometry
        self.dict_kargs[holetype] = {self.dict_geometry_mp[holetype][0]: self.radius}

    def plot_geometry(self, scale=1.0 / 3.0):
        dict_geometry = self.get_geometry()
        cols = list(dict_geometry.keys())
        plt.figure(figsize=(self.ny * scale, self.nx * scale * np.sqrt(3)))
        plt.scatter(dict_geometry[cols[0]][:, 0], dict_geometry[cols[0]][:, 1])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


# -----------------------------------------------------------------------------
# Inlined from parse_to_meep.py
# -----------------------------------------------------------------------------
DICT_GEOMETRY_MP = {
    "circle": mp.Cylinder,
    "triangle": mp.Prism,
    "block": mp.Block,
}


def parse_geometry(obj_phc, thick_slab=0):
    """Convert a GeometryPhC-like object into a flat list of Meep objects."""
    arr_obj = []
    dict_geometry = obj_phc.get_geometry()
    dict_kargs = obj_phc.get_kargs()

    for key, npr_geometry in dict_geometry.items():
        ptr_mpobj = DICT_GEOMETRY_MP[key]
        kargs = dict_kargs[key]
        list_obj = []

        for x, y in npr_geometry:
            list_obj.append(ptr_mpobj(center=mp.Vector3(x, y, thick_slab), **kargs))

        arr_obj.extend(list_obj)

    return arr_obj



# -----------------------------------------------------------------------------
# Inlined from transmittance.py
# -----------------------------------------------------------------------------
class MeepTransmittance:
    """Reference straight-waveguide transmittance calculator."""

    def __init__(
        self,
        sim=None,
        endpoint=mp.Vector3(),
        tran_out=None,
        dim=2,
        area_z=8,
        thick_slab=0,
        fcen=0.25,
        df=0.05,
        thres_conv=1e-3,
        nfreq=500,
        resolution=16,
        dpml=1,
    ) -> None:
        self.sim = sim
        self.endpoint = endpoint
        self.tran_out = tran_out
        self.fcen = fcen
        self.df = df
        self.dict_thick_slab = {2: mp.inf, 3: thick_slab}
        self.dict_area_z = {2: 0, 3: area_z}
        self.dict_beamz = {2: 0, 3: thick_slab}
        self.area_z = self.dict_area_z[dim]
        self.beamz = self.dict_beamz[dim]
        self.dim = dim
        self.thick_slab = self.dict_thick_slab[dim]
        self.thres_conv = thres_conv
        self.nfreq = nfreq
        self.resolution = resolution
        self.dpml = dpml

    def get_reference_transmittance(
        self,
        a=1,
        nx=5,
        ny=30,
        len_siwg=10,
        eps_r=2.6**2,
        wg=1,
        pml_buffer=2,
    ):
        """Calculate the transmittance of the reference straight waveguide."""
        cell = mp.Vector3(
            a * (ny + pml_buffer + len_siwg * 2 + self.dpml - 1),
            a * (nx + pml_buffer / 2) * np.sqrt(3),
            self.area_z,
        )

        arr_wg = [
            mp.Block(
                mp.Vector3(
                    a * (ny + 2 * (len_siwg + pml_buffer + self.dpml - 1)),
                    wg * np.sqrt(3),
                    self.thick_slab,
                ),
                center=mp.Vector3(0, 0),
                material=mp.Medium(epsilon=eps_r),
            )
        ]

        src = [
            mp.Source(
                mp.GaussianSource(self.fcen, fwidth=self.df),
                component=mp.Hz,
                center=mp.Vector3(-a * (ny / 2 + len_siwg - (self.dpml - 1) / 2), 0),
                size=mp.Vector3(0, wg * np.sqrt(3), self.beamz),
            )
        ]

        sym = [mp.Mirror(mp.Y, phase=-1)]
        if self.dim == 3:
            sym.append(mp.Mirror(mp.Z, phase=1))

        pml_layers = [mp.PML(self.dpml)]

        self.sim_ref = mp.Simulation(
            cell_size=cell,
            geometry=arr_wg,
            boundary_layers=pml_layers,
            sources=src,
            dimensions=self.dim,
            symmetries=sym,
            resolution=self.resolution,
        )

        vec_out = mp.Vector3(a * (ny / 2 + len_siwg - 1 + (self.dpml - 2) / 2), 0)
        tran_out = mp.FluxRegion(center=vec_out, size=mp.Vector3(0, 2 * wg, self.beamz))
        trans_out = self.sim_ref.add_flux(self.fcen, self.df, self.nfreq, tran_out)

        if self.dim == 2:
            fig = plt.figure(dpi=100)
            self.sim_ref.plot2D(ax=fig.gca())
            plt.show()

        self.sim_ref.run(
            until_after_sources=mp.stop_when_fields_decayed(50, mp.Hz, vec_out, self.thres_conv)
        )

        self.freqs_ref = np.array(mp.get_flux_freqs(trans_out))
        self.psd_out = np.array(mp.get_fluxes(trans_out))

        return self.freqs_ref, self.psd_out

    def plot_reference_transmittance(self):
        plt.figure(figsize=(6, 4))
        plt.plot(self.freqs_ref, self.psd_out, label="Reference")
        plt.xlabel("Frequency")
        plt.ylabel("Power Spectral Density")
        plt.yscale("log")
        plt.legend()
        plt.tight_layout()
        plt.show()


# -----------------------------------------------------------------------------
# Main simulation
# -----------------------------------------------------------------------------
def main():
    # mpirun -np 4 python transmittance_3DW1waveguide_standalone.py

    # Settings of geometry
    a = 1  # 0.4
    nx = 10  # 14
    ny = 20  # 50
    offset_x = 0
    offset_y = 0
    barrier = 6
    wgo = 1
    wgi = 1
    holeshift = 0

    # 3D component
    hslab = 0.5
    h = 8

    # Connection waveguide
    len_siwg = 10  # length of straight input/output waveguide
    eps_r = 3.48**2
    fcen = 0.25
    df = 0.1
    resolution = 16
    pml_buffer = 2
    nfreq = 500
    thres_conv = 1e-3  # 1e-7

    os.makedirs("outputs", exist_ok=True)

    # Area of simulation cell
    cell = mp.Vector3(a * (ny + pml_buffer + len_siwg * 2), a * (nx + 3) * np.sqrt(3), h)

    # Air
    arr_air = [
        mp.Block(
            size=mp.Vector3(a * (ny + pml_buffer + len_siwg * 2), a * (nx + 3) * np.sqrt(3), h),
            material=mp.Medium(epsilon=1),
        )
    ]

    # Bulk material
    arr_blk = [
        mp.Block(
            size=mp.Vector3(a * ny, a * (nx + 3) * np.sqrt(3), hslab),
            material=mp.Medium(epsilon=eps_r),
        )
    ]

    # Waveguide
    arr_wg = [
        mp.Block(
            mp.Vector3(a * (len_siwg + pml_buffer), wgi * np.sqrt(3), hslab),
            center=mp.Vector3(-a * (ny / 2 + (len_siwg + pml_buffer) / 2), 0),
            material=mp.Medium(epsilon=eps_r),
        ),
        mp.Block(
            mp.Vector3(a * (len_siwg + pml_buffer), wgi * np.sqrt(3), hslab),
            center=mp.Vector3(a * (ny / 2 + (len_siwg + pml_buffer) / 2), 0),
            material=mp.Medium(epsilon=eps_r),
        ),
    ]

    # Photonic crystal cavity
    wm = WidthModulated(a, nx, ny, offset_x, offset_y, barrier, wgo, wgi, holeshift)
    arr_obj = parse_geometry(wm, thick_slab=hslab)

    # All geometry
    arr_geometry = arr_air + arr_blk + arr_wg + arr_obj

    # Source
    src = [
        mp.Source(
            mp.GaussianSource(fcen, fwidth=df),
            component=mp.Hz,
            center=mp.Vector3(-a * (ny / 2 + len_siwg), 0),
            size=mp.Vector3(0, wgi * np.sqrt(3), hslab),
        )
    ]

    # Symmetry
    sym = [mp.Mirror(mp.Y, phase=-1), mp.Mirror(mp.Z, phase=1)]

    # PML
    pml_layers = [mp.PML(1.0)]

    # Build simulation object
    sim = mp.Simulation(
        cell_size=cell,
        geometry=arr_geometry,
        boundary_layers=pml_layers,
        sources=src,
        symmetries=sym,
        dimensions=3,
        resolution=resolution,
    )

    # Output flux
    vec_out = mp.Vector3(a * (ny / 2 + len_siwg - 1), 0, 0)
    tran_out = mp.FluxRegion(center=vec_out, size=mp.Vector3(0, 2 * wgi, hslab))
    trans_out = sim.add_flux(fcen, df, nfreq, tran_out)

    sim.init_sim()
    eps_data = sim.get_epsilon()
    _ = eps_data  # Keep eps_data available for interactive/debug use.

    # Run simulation
    sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Hz, vec_out, thres_conv))

    freqs = np.array(mp.get_flux_freqs(trans_out))
    psd_out = np.array(mp.get_fluxes(trans_out))

    df_phcraw = pd.DataFrame(np.array([freqs, psd_out]).T, columns=["freq", "transmittance"])
    df_phcraw.to_csv(OUT_DIR / "transmittance_raw_3DW1waveguide.csv", index=False)

    # Reference
    cls_ref = MeepTransmittance(
        dim=3,
        area_z=h,
        thick_slab=hslab,
        fcen=fcen,
        df=df,
        thres_conv=thres_conv,
        nfreq=nfreq,
        resolution=resolution,
        dpml=1,
    )
    freqs_ref, psd_ref = cls_ref.get_reference_transmittance(
        a=a,
        nx=nx,
        ny=ny,
        len_siwg=len_siwg,
        eps_r=eps_r,
        wg=wgi,
        pml_buffer=pml_buffer,
    )

    lattice_const = 400
    wl = lattice_const / freqs_ref
    df_ref = pd.DataFrame(np.array([freqs_ref, wl, psd_ref]).T, columns=["freq", "wl", "transmittance"])
    df_ref.to_csv(OUT_DIR / "transmittance_3D_refwaveguide.csv", index=False)

    trans_norm = psd_out / psd_ref
    df_phc = pd.DataFrame(np.array([freqs_ref, wl, trans_norm]).T, columns=["freq", "wl", "transmittance"])
    df_phc.to_csv(OUT_DIR / "transmittance_3DW1waveguide.csv", index=False)

    # Plot frequency-domain transmittance
    plt.figure(figsize=(8, 6))
    plt.plot(freqs, trans_norm, label="W1", marker="o", markersize=3)
    plt.xlabel("Frequency")
    plt.ylabel("Intensity")
    plt.yscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "transmittance_3DW1waveguide.svg")
    plt.show()

    # Plot wavelength-domain transmittance
    plt.figure(figsize=(8, 6))
    plt.plot(wl, trans_norm, label="W1", marker="o", markersize=3, color="black")
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Intensity")
    plt.yscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "transmittance_wl_3DW1waveguide.svg")
    plt.show()


if __name__ == "__main__":
    main()

# %%
