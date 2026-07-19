#%%
import meep as mp
from meep import mpb
import numpy as np


from pathlib import Path
import os

script_dir = Path(__file__).resolve().parent
fig_dir = script_dir / "fig"
out_dir = script_dir / "out"
fig_dir.mkdir(exist_ok=True)
out_dir.mkdir(exist_ok=True)
os.chdir(out_dir)

# configuration
n_air = 1
n_si = 3.48
a = 1
num_bands = 3 #計算する固有周波数の数
resolution = 16 #メッシュの細かさ
num_k = 0#5#10 #Γ-K, K-M, M-Γ間の点の個数

"""
s0 ... one side of triangular hole
h = 0.5*a ... slab thickness
radius_pole ... radius of pole circles
s1 = s0 * 0.5 ... position of pole circles from center triangle
"""

def gap_tri(h = 1.2*a, r1 = 0.14*a, r2 = 0.38*a):
    geometry_lattice = mp.Lattice(size=mp.Vector3(1, 1, 10*h),
                                basis1=mp.Vector3(1./2, np.sqrt(3)/2),
                                basis2=mp.Vector3(1./2, -np.sqrt(3)/2))

    geometry = [
        mp.Block(material=mp.Medium(epsilon=1),
                size=mp.Vector3(mp.inf, mp.inf, 10*h)),
        mp.Block(material=mp.Medium(epsilon=n_si**2),
                size=mp.Vector3(mp.inf, mp.inf, h)),
        mp.Cylinder(r1, center=mp.Vector3(2, 1)/3, 
                    material=mp.Medium(epsilon=n_air**2)),
        mp.Cylinder(r2, center=mp.Vector3(1, 2)/3, 
                    material=mp.Medium(epsilon=n_air**2)),
    ]

    #ブリルアンゾーン
    k_points = [
        #mp.Vector3(),               # Gamma
        mp.Vector3(1./3, 1./3),    # K
        mp.Vector3(1./2, 0),          # M
        #mp.Vector3(),               # Gamma
    ]
    k_points = mp.interpolate(num_k, k_points)

    #計算
    ms = mpb.ModeSolver(
        geometry=geometry,
        geometry_lattice=geometry_lattice,
        k_points=k_points,
        resolution=resolution,
        num_bands=num_bands
    )

    ms.run_tm(mpb.output_at_kpoint(mp.Vector3(1./3, 1./3),
                                mpb.fix_efield_phase,
                                mpb.output_efield_z))
    tm_freqs = ms.all_freqs
    ms.run_te(mpb.output_at_kpoint(mp.Vector3(1./3, 1./3),
                                mpb.fix_efield_phase,
                                mpb.output_efield_z))
    te_freqs = ms.all_freqs

    idx_k = 0#num_k+1
    idx_m = 1#2*(num_k+1)

    f_te1_k = te_freqs[idx_k,0]
    f_te2_k = te_freqs[idx_k,1]
    f_te1_m = te_freqs[idx_m,0]
    f_te2_m = te_freqs[idx_m,1]
    f_tm1_k = tm_freqs[idx_k,0]
    f_tm2_k = tm_freqs[idx_k,1]
    f_tm1_m = tm_freqs[idx_m,0]
    f_tm2_m = tm_freqs[idx_m,1]

    lap = [0]*6
    # Bandgap of TE, TM
    lap[0] = min(f_tm2_k, f_tm2_m) - max(f_tm1_k, f_tm1_m)
    lap[1] = min(f_te2_k, f_te2_m) - max(f_te1_k, f_te1_m)
    # Overlap bandgap between band 1 and 2
    lap[2] = min(f_tm2_k, f_tm2_m) - max(f_te1_k, f_te1_m)
    lap[3] = min(f_te2_k, f_te2_m) - max(f_tm1_k, f_tm1_m)
    
    lap[4] = max(f_tm2_k, f_tm2_m) - min(f_te1_k, f_te1_m)
    lap[5] = max(f_te2_k, f_te2_m) - min(f_tm1_k, f_tm1_m)
    
    minlap = min(lap)
    print("\n\n\n\n\n\n\n")
    print("Overlap bandgap between band 1 and 2:", minlap)
    print("\n\n\n\n\n\n\n")

    return minlap


if __name__ == "__main__":
    h, r1, r2 = (1.2, 0.14, 0.38)

    # optimization
    import scipy.optimize as opt

    def gap_tri_opt(x):
        return -gap_tri(h=x[0], r1=x[1], r2=x[2])

    x0 = np.array([h, r1, r2])
    bounds = [(0, 1.5), (0, 0.45), (0, 0.45)] 
    res = opt.minimize(gap_tri_opt, x0, bounds=bounds, method='Nelder-Mead')  # "SLSQP", options={"maxiter":1})
    print(res)


    import pandas as pd
    pd.DataFrame(res.x).to_csv(out_dir / "opt_result.csv")

    print("Done!")



# %%
