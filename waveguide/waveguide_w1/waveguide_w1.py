#%%
import time
import math
import meep as mp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



from pathlib import Path

script_dir = Path(__file__).resolve().parent
fig_dir = script_dir / "fig"
out_dir = script_dir / "out"
fig_dir.mkdir(exist_ok=True)
out_dir.mkdir(exist_ok=True)

#path = "output/"

def phc_trans(use_photonic_crystal = True, photonic_crystal_length = 100, decay_check=0, decay_time=500):
    """
    <変数の説明>
    PhC...PhC(フォトニック決勝)を配置するかどうか。Falseで直線導波路
    photonic_crystal_length...PhC導波方向の長さ
    photonic_crystal_width...PhC垂直方向の幅。PMLと被ってるので適当。
    connection_waveguide...PhCに接続するSi導波路(棒の部分)の長さ
    wgi...導波路の幅を調整する。1で丸穴一個分空いてることを意味する。0.7とかにすると狭くなってバンドの形が変わる、っていうのはDaii君の研究とも絡む。
    r...穴の半径。ふつうはa/4くらい。meepだと格子定数は1で固定だから、格子定数との比を入力すればOK
    n_eff...屈折率。2次元だと2.5~2.7くらいにしておくと3次元のSi系(n_si=3.48)と結果が近くなる。違う材料を使うときは要調整、通常はdefaultで大丈夫。
    fcen...入力光（ガウシアンビーム）の中心周波数。知りたいPhCバンドの周波数近くに設定する
    df...入力光（ガウシアンビーム）の半値幅（で合ってる？）
    nfreq...入力光（ガウシアンビーム）のきめ細かさ
    resolution...メッシュの細かさ。2^nにすると計算が軽くなるらしい。
    decay_time...反復計算数。小さいと誤差が増え、大きいと時間がかかる。sim.run(until_after_sources=...)で計算時間を見積もってから変えるとよさそう
    decay_check...解の収束をどこで判定するか、位置を指定。defaultでOK

    <備考>
    ・meepでは格子定数aはパラメータに含まれないので設定不要
    　誘電体を使うときは入力するらしい（スケール依存性が出るから）
    ・THzやnmは使用せず、すべて規格化周波数で入力する (周波数はωa/2πcで直す)
    """
    ##### setting of parameters #####
    photonic_crystal_width = 10
    connection_waveguide = 5
    wgi = 1
    r = 1/4
    n_eff = 2.6
    fcen = 0.3 
    df = 0.1
    nfreq = 500 # number of frequencies at which to compute flux
    resolution = 16
    
    #####
    length = photonic_crystal_length + 2*connection_waveguide
    width = photonic_crystal_width
    nx = int(photonic_crystal_length)
    ny = int(photonic_crystal_width)
    eps = n_eff**2

    ##### settings of geometry #####
    # initialization
    cell = mp.Vector3(length,width*np.sqrt(3),0)

    # Si waveguide
    waveguide = mp.Block(mp.Vector3(mp.inf,wgi*np.sqrt(3),mp.inf),
                         center=mp.Vector3(),
                         material=mp.Medium(epsilon=eps))
    geometry = [waveguide]

    # PhC
    if use_photonic_crystal:
        # slab
        blk = mp.Block(mp.Vector3(photonic_crystal_length,photonic_crystal_width*np.sqrt(3),mp.inf),
                             center=mp.Vector3(),
                             material=mp.Medium(epsilon=eps))

        geometry.append(blk)
        
        # arrange air-holes
        for j in range(ny):
            for i in range(nx+1):
                shift_y = np.sqrt(3)
                geometry.append(mp.Cylinder(r, center=mp.Vector3(i-nx/2, wgi*np.sqrt(3)/2 + shift_y*j)))
                geometry.append(mp.Cylinder(r, center=mp.Vector3(i-nx/2, -(wgi*np.sqrt(3)/2 + shift_y*j))))

                geometry.append(mp.Cylinder(r, center=mp.Vector3(i-(nx+1)/2, wgi*np.sqrt(3)/2 + shift_y*(j+1/2))))
                geometry.append(mp.Cylinder(r, center=mp.Vector3(i-(nx+1)/2, -(wgi*np.sqrt(3)/2 + shift_y*(j+1/2)))))
                #geometry.append(mp.Cylinder(r, center=mp.Vector3(i-N/2,-wgi*np.sqrt(3)/2)))
    
    # Gaussian
    sources = [mp.Source(mp.GaussianSource(fcen, fwidth=df),
                         component=mp.Hz,
                         center=mp.Vector3(-length/2 +1,0),
                         size=mp.Vector3(0,wgi*np.sqrt(3)))
              ]

    # PML
    pml_layers = [mp.PML(1.0)]

    # z-symmetry (上下対称なら計算が軽くなる。対称性が無いなら消す)
    sym = [mp.Mirror(mp.Y, phase=-1)]
    

    ####
    sim = mp.Simulation(cell_size=cell,
                        boundary_layers=pml_layers,
                        geometry=geometry,
                        sources=sources,
                        symmetries=sym,
                        resolution=resolution)

    #tran_in = mp.FluxRegion(center=mp.Vector3(-photonic_crystal_length/2-1,0),size=mp.Vector3(0, 2*wgi))
    tran_out = mp.FluxRegion(center=mp.Vector3(length/2-3/2,0),size=mp.Vector3(0, 2*wgi))
    #trans_in = sim.add_flux(fcen, df, nfreq, tran_in)
    trans_out = sim.add_flux(fcen, df, nfreq, tran_out)

    # Plot geometry
    f = plt.figure(dpi=100)
    sim.plot2D(ax=f.gca())
    plt.show()
    # show geometry
    #f = plt.figure(dpi=150)
    #sim.plot2D(ax=f.gca())
    # plt.show()
    if use_photonic_crystal:
        filename = "geometry_phc"
    else:
        filename = "geometry_siwaveguide"
    #plt.savefig(fig_dir / (filename + ".png"))


    # sim.run(until=decay_time)
    # 電場が減衰するまでしっかり計算する場合は、下を使う
    sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Hz, mp.Vector3(decay_check), 1e-7))

    freqs = mp.get_flux_freqs(trans_out)
    #psd_in = mp.get_fluxes(trans_in)
    psd_out = mp.get_fluxes(trans_out)

    return freqs, psd_out


if __name__ == "__main__":  
    time_start = time.perf_counter()

    a = 400
    c_const = 299792458
    freqs_wo, psd_out_wo = phc_trans(use_photonic_crystal = False, photonic_crystal_length = 20, decay_check=10, decay_time=500)
    freqs_w,  psd_out_w  = phc_trans(use_photonic_crystal = True, photonic_crystal_length = 40, decay_check=20, decay_time=10000)

    freqs = a / np.array(freqs_w)


    df = pd.DataFrame()
    df["normalized_frequency"] = np.array(freqs_w)
    df["wavelength"] = freqs
    df["transmittance"] = np.array(psd_out_w)/np.array(psd_out_wo)
    df.to_csv(out_dir / "transmittance1.csv", index=False)

    """
    plt.plot(freqs, np.array(psd_out_w)/np.array(psd_out_wo))
    plt.scatter(freqs, np.array(psd_out_w)/np.array(psd_out_wo))
    plt.xlabel("Frequency[c/a]")
    plt.ylabel("Transmittance[c/a]")
    #plt.xlim([0.28,0.30])
    plt.yscale('log')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(fig_dir / "phcwaveguide_transmittance1.png")
    """
    time_end = time.perf_counter()
    time = time_end - time_start
    print("The necessary time: {:.3f}s".format(time))

    f = open(out_dir / 'totaltime1.txt', 'w')
    f.write("The necessary time: {:.3f}s".format(time))
    f.close()
# %%
