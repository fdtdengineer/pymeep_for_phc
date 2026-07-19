# -*- coding: utf-8 -*-
# Materials Library

import meep as mp
import numpy as np

# default unit length is 1 um
um_scale = 1.0

# conversion factor for eV to 1/um [=1/hc]
e_v_um_scale = um_scale/1.23984193

#------------------------------------------------------------------
# crystalline silicon (c-Si) from A. Deinega et al., J. Optical Society of America A, Vol. 28, No. 5, pp. 770-77, 2011
# based on experimental data for intrinsic silicon at T=300K from M.A. Green and M. Keevers, Progress in Photovoltaics, Vol. 3, pp. 189-92, 1995
# wavelength range: 0.4 - 1.0 um

c_si_range = mp.FreqRange(min=um_scale, max=um_scale/0.4)

c_si_frq1 = 3.64/um_scale
c_si_gam1 = 0
c_si_sig1 = 8
c_si_frq2 = 2.76/um_scale
c_si_gam2 = 2*0.063/um_scale
c_si_sig2 = 2.85
c_si_frq3 = 1.73/um_scale
c_si_gam3 = 2*2.5/um_scale
c_si_sig3 = -0.107

c_si_susc = [mp.LorentzianSusceptibility(frequency=c_si_frq1, gamma=c_si_gam1, sigma=c_si_sig1),
            mp.LorentzianSusceptibility(frequency=c_si_frq2, gamma=c_si_gam2, sigma=c_si_sig2),
            mp.LorentzianSusceptibility(frequency=c_si_frq3, gamma=c_si_gam3, sigma=c_si_sig3)]

c_si = mp.Medium(epsilon=1.0, E_susceptibilities=c_si_susc, valid_freq_range=c_si_range)

#------------------------------------------------------------------
# amorphous silicon (a-Si) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.21 - 0.83 um

a_si_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.21)

a_si_frq1 = 1/(0.315481407124682*um_scale)
a_si_gam1 = 1/(0.645751005208333*um_scale)
a_si_sig1 = 14.571

a_si_susc = [mp.LorentzianSusceptibility(frequency=a_si_frq1, gamma=a_si_gam1, sigma=a_si_sig1)]

a_si = mp.Medium(epsilon=3.109, E_susceptibilities=a_si_susc, valid_freq_range=a_si_range)

#------------------------------------------------------------------
# hydrogenated amorphous silicon (a-Si:H) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.21 - 0.83 um

a_si_h_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.21)

a_si_h_frq1 = 1/(0.334189199460916*um_scale)
a_si_h_gam1 = 1/(0.579365387850467*um_scale)
a_si_h_sig1 = 12.31

a_si_h_susc = [mp.LorentzianSusceptibility(frequency=a_si_h_frq1, gamma=a_si_h_gam1, sigma=a_si_h_sig1)]

a_si_h = mp.Medium(epsilon=3.22, E_susceptibilities=a_si_h_susc, valid_freq_range=a_si_h_range)

#------------------------------------------------------------------
# indium tin oxide (ITO) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.21 - 0.83 um

ito_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.21)

ito_frq1 = 1/(0.182329695588235*um_scale)
ito_gam1 = 1/(1.94637665620094*um_scale)
ito_sig1 = 2.5

ito_susc = [mp.LorentzianSusceptibility(frequency=ito_frq1, gamma=ito_gam1, sigma=ito_sig1)]

ito = mp.Medium(epsilon=1.0, E_susceptibilities=ito_susc, valid_freq_range=ito_range)

#------------------------------------------------------------------
# alumina (Al2O3) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.21 - 2.07 um

al2_o3_range = mp.FreqRange(min=um_scale/2.07, max=um_scale/0.21)

al2_o3_frq1 = 1/(0.101476668030774*um_scale)
al2_o3_gam1 = 0
al2_o3_sig1 = 1.52

al2_o3_susc = [mp.LorentzianSusceptibility(frequency=al2_o3_frq1, gamma=al2_o3_gam1, sigma=al2_o3_sig1)]

al2_o3 = mp.Medium(epsilon=1.0, E_susceptibilities=al2_o3_susc, valid_freq_range=al2_o3_range)

#------------------------------------------------------------------
# aluminum nitride (AlN) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.26 - 1.65 um

al_n_range = mp.FreqRange(min=um_scale/1.65, max=um_scale/0.26)

al_n_frq1 = 1/(0.139058089950651*um_scale)
al_n_gam1 = 0
al_n_sig1 = 3.306

al_n_susc = [mp.LorentzianSusceptibility(frequency=al_n_frq1, gamma=al_n_gam1, sigma=al_n_sig1)]

al_n = mp.Medium(epsilon=1.0, E_susceptibilities=al_n_susc, valid_freq_range=al_n_range)

#------------------------------------------------------------------
# aluminum arsenide (AlAs) from R.E. Fern and A. Onton, J. Applied Physics, Vol. 42, pp. 3499-500, 1971
# ref: https://refractiveindex.info/?shelf=main&book=AlAs&page=Fern
# wavelength range: 0.56 - 2.2 um

al_as_range = mp.FreqRange(min=um_scale/2.2, max=um_scale/0.56)

al_as_frq1 = 1/(0.2822*um_scale)
al_as_gam1 = 0
al_as_sig1 = 6.0840
al_as_frq2 = 1/(27.62*um_scale)
al_as_gam2 = 0
al_as_sig2 = 1.900

al_as_susc = [mp.LorentzianSusceptibility(frequency=al_as_frq1, gamma=al_as_gam1, sigma=al_as_sig1),
             mp.LorentzianSusceptibility(frequency=al_as_frq2, gamma=al_as_gam2, sigma=al_as_sig2)]

al_as = mp.Medium(epsilon=2.0792, E_susceptibilities=al_as_susc, valid_freq_range=al_as_range)

#------------------------------------------------------------------
# borosilicate glass (BK7) from SCHOTT Zemax catalog 2017-01-20b
# ref: https://refractiveindex.info/?shelf=glass&book=BK7&page=SCHOTT
# wavelength range: 0.3 - 2.5 um

bk7_range = mp.FreqRange(min=um_scale/2.5, max=um_scale/0.3)

bk7_frq1 = 1/(0.07746417668832478*um_scale)
bk7_gam1 = 0
bk7_sig1 = 1.03961212
bk7_frq2 = 1/(0.14148467902921502*um_scale)
bk7_gam2 = 0
bk7_sig2 = 0.231792344
bk7_frq3 = 1/(10.176475470417055*um_scale)
bk7_gam3 = 0
bk7_sig3 = 1.01046945

bk7_susc = [mp.LorentzianSusceptibility(frequency=bk7_frq1, gamma=bk7_gam1, sigma=bk7_sig1),
            mp.LorentzianSusceptibility(frequency=bk7_frq2, gamma=bk7_gam2, sigma=bk7_sig2),
            mp.LorentzianSusceptibility(frequency=bk7_frq3, gamma=bk7_gam3, sigma=bk7_sig3)]

bk7 = mp.Medium(epsilon=1.0, E_susceptibilities=bk7_susc, valid_freq_range=bk7_range)

#------------------------------------------------------------------
# fused quartz (silica) from I.H. Malitson, J. Optical Society of America, Vol. 55, pp. 1205-9, 1965
# ref: https://refractiveindex.info/?shelf=glass&book=fused_silica&page=Malitson
# wavelength range: 0.21 - 6.7 um

fused_quartz_range = mp.FreqRange(min=um_scale/6.7, max=um_scale/0.21)

fused_quartz_frq1 = 1/(0.0684043*um_scale)
fused_quartz_gam1 = 0
fused_quartz_sig1 = 0.696166300
fused_quartz_frq2 = 1/(0.1162414*um_scale)
fused_quartz_gam2 = 0
fused_quartz_sig2 = 0.407942600
fused_quartz_frq3 = 1/(9.896161*um_scale)
fused_quartz_gam3 = 0
fused_quartz_sig3 = 0.897479400

fused_quartz_susc = [mp.LorentzianSusceptibility(frequency=fused_quartz_frq1, gamma=fused_quartz_gam1, sigma=fused_quartz_sig1),
                     mp.LorentzianSusceptibility(frequency=fused_quartz_frq2, gamma=fused_quartz_gam2, sigma=fused_quartz_sig2),
                     mp.LorentzianSusceptibility(frequency=fused_quartz_frq3, gamma=fused_quartz_gam3, sigma=fused_quartz_sig3)]

fused_quartz = mp.Medium(epsilon=1.0, E_susceptibilities=fused_quartz_susc, valid_freq_range=fused_quartz_range)

#------------------------------------------------------------------
# gallium arsenide (GaAs) from T. Skauli et al., J. Applied Physics, Vol. 94, pp. 6447-55, 2003
# ref: https://refractiveindex.info/?shelf=main&book=GaAs&page=Skauli
# wavelength range: 0.97 - 17 um

ga_as_range = mp.FreqRange(min=um_scale/17, max=um_scale/0.97)

ga_as_frq1 = 1/(0.4431307*um_scale)
ga_as_gam1 = 0
ga_as_sig1 = 5.466742
ga_as_frq2 = 1/(0.8746453*um_scale)
ga_as_gam2 = 0
ga_as_sig2 = 0.02429960
ga_as_frq3 = 1/(36.9166*um_scale)
ga_as_gam3 = 0
ga_as_sig3 = 1.957522

ga_as_susc = [mp.LorentzianSusceptibility(frequency=ga_as_frq1, gamma=ga_as_gam1, sigma=ga_as_sig1),
             mp.LorentzianSusceptibility(frequency=ga_as_frq2, gamma=ga_as_gam2, sigma=ga_as_sig2),
             mp.LorentzianSusceptibility(frequency=ga_as_frq3, gamma=ga_as_gam3, sigma=ga_as_sig3)]

ga_as = mp.Medium(epsilon=5.372514, E_susceptibilities=ga_as_susc, valid_freq_range=ga_as_range)

#------------------------------------------------------------------
# silicon nitride (Si3N4) from H. R. Philipp, J. Electrochemical Society 120, 295-300, 1973
# ref: https://refractiveindex.info/?shelf=main&book=Si3N4&page=Philipp
# wavelength range: 0.207 - 1.24 um

si3_n4_visnir_range = mp.FreqRange(min=um_scale/1.24, max=um_scale/0.207)

si3_n4_visnir_frq1 = 1/(0.13967*um_scale)
si3_n4_visnir_gam1 = 0
si3_n4_visnir_sig1 = 2.8939

si3_n4_visnir_susc = [mp.LorentzianSusceptibility(frequency=si3_n4_visnir_frq1, gamma=si3_n4_visnir_gam1, sigma=si3_n4_visnir_sig1)]

si3_n4_visnir = mp.Medium(epsilon=1.0, E_susceptibilities=si3_n4_visnir_susc, valid_freq_range=si3_n4_visnir_range)

#------------------------------------------------------------------
# silicon nitride (Si3N4) from K. Luke, et. al., Optics Letters, Vol. 40, pp. 4823-26, 2015
# ref: https://refractiveindex.info/?shelf=main&book=Si3N4&page=Luke
# wavelength range: 0.310 - 5.504 um

si3_n4_nir_range = mp.FreqRange(min=um_scale/5.504, max=um_scale/0.310)

si3_n4_nir_frq1 = 1/(0.1353406*um_scale)
si3_n4_nir_gam1 = 0
si3_n4_nir_sig1 = 3.0249
si3_n4_nir_frq2 = 1/(1239.842*um_scale)
si3_n4_nir_gam2 = 0
si3_n4_nir_sig2 = 40314

si3_n4_nir_susc = [mp.LorentzianSusceptibility(frequency=si3_n4_nir_frq1, gamma=si3_n4_nir_gam1, sigma=si3_n4_nir_sig1),
                  mp.LorentzianSusceptibility(frequency=si3_n4_nir_frq2, gamma=si3_n4_nir_gam2, sigma=si3_n4_nir_sig2)]

si3_n4_nir = mp.Medium(epsilon=1.0, E_susceptibilities=si3_n4_nir_susc, valid_freq_range=si3_n4_nir_range)

#------------------------------------------------------------------
# elemental metals from A.D. Rakic et al., Applied Optics, Vol. 37, No. 22, pp. 5271-83, 1998
# wavelength range: 0.2 - 12.4 um

metal_range = mp.FreqRange(min=um_scale/12.398, max=um_scale/.24797)

# silver (Ag)

ag_plasma_frq = 9.01*e_v_um_scale
ag_f0 = 0.845
ag_frq0 = 1e-10
ag_gam0 = 0.048*e_v_um_scale
ag_sig0 = ag_f0*ag_plasma_frq**2/ag_frq0**2
ag_f1 = 0.065
ag_frq1 = 0.816*e_v_um_scale      # 1.519 um
ag_gam1 = 3.886*e_v_um_scale
ag_sig1 = ag_f1*ag_plasma_frq**2/ag_frq1**2
ag_f2 = 0.124
ag_frq2 = 4.481*e_v_um_scale      # 0.273 um
ag_gam2 = 0.452*e_v_um_scale
ag_sig2 = ag_f2*ag_plasma_frq**2/ag_frq2**2
ag_f3 = 0.011
ag_frq3 = 8.185*e_v_um_scale      # 0.152 um
ag_gam3 = 0.065*e_v_um_scale
ag_sig3 = ag_f3*ag_plasma_frq**2/ag_frq3**2
ag_f4 = 0.840
ag_frq4 = 9.083*e_v_um_scale      # 0.137 um
ag_gam4 = 0.916*e_v_um_scale
ag_sig4 = ag_f4*ag_plasma_frq**2/ag_frq4**2
ag_f5 = 5.646
ag_frq5 = 20.29*e_v_um_scale      # 0.061 um
ag_gam5 = 2.419*e_v_um_scale
ag_sig5 = ag_f5*ag_plasma_frq**2/ag_frq5**2

ag_susc = [mp.DrudeSusceptibility(frequency=ag_frq0, gamma=ag_gam0, sigma=ag_sig0),
           mp.LorentzianSusceptibility(frequency=ag_frq1, gamma=ag_gam1, sigma=ag_sig1),
           mp.LorentzianSusceptibility(frequency=ag_frq2, gamma=ag_gam2, sigma=ag_sig2),
           mp.LorentzianSusceptibility(frequency=ag_frq3, gamma=ag_gam3, sigma=ag_sig3),
           mp.LorentzianSusceptibility(frequency=ag_frq4, gamma=ag_gam4, sigma=ag_sig4),
           mp.LorentzianSusceptibility(frequency=ag_frq5, gamma=ag_gam5, sigma=ag_sig5)]

ag = mp.Medium(epsilon=1.0, E_susceptibilities=ag_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# gold (Au)

metal_range = mp.FreqRange(min=um_scale/6.1992, max=um_scale/.24797)

au_plasma_frq = 9.03*e_v_um_scale
au_f0 = 0.760
au_frq0 = 1e-10
au_gam0 = 0.053*e_v_um_scale
au_sig0 = au_f0*au_plasma_frq**2/au_frq0**2
au_f1 = 0.024
au_frq1 = 0.415*e_v_um_scale      # 2.988 um
au_gam1 = 0.241*e_v_um_scale
au_sig1 = au_f1*au_plasma_frq**2/au_frq1**2
au_f2 = 0.010
au_frq2 = 0.830*e_v_um_scale      # 1.494 um
au_gam2 = 0.345*e_v_um_scale
au_sig2 = au_f2*au_plasma_frq**2/au_frq2**2
au_f3 = 0.071
au_frq3 = 2.969*e_v_um_scale      # 0.418 um
au_gam3 = 0.870*e_v_um_scale
au_sig3 = au_f3*au_plasma_frq**2/au_frq3**2
au_f4 = 0.601
au_frq4 = 4.304*e_v_um_scale      # 0.288 um
au_gam4 = 2.494*e_v_um_scale
au_sig4 = au_f4*au_plasma_frq**2/au_frq4**2
au_f5 = 4.384
au_frq5 = 13.32*e_v_um_scale      # 0.093 um
au_gam5 = 2.214*e_v_um_scale
au_sig5 = au_f5*au_plasma_frq**2/au_frq5**2

au_susc = [mp.DrudeSusceptibility(frequency=au_frq0, gamma=au_gam0, sigma=au_sig0),
           mp.LorentzianSusceptibility(frequency=au_frq1, gamma=au_gam1, sigma=au_sig1),
           mp.LorentzianSusceptibility(frequency=au_frq2, gamma=au_gam2, sigma=au_sig2),
           mp.LorentzianSusceptibility(frequency=au_frq3, gamma=au_gam3, sigma=au_sig3),
           mp.LorentzianSusceptibility(frequency=au_frq4, gamma=au_gam4, sigma=au_sig4),
           mp.LorentzianSusceptibility(frequency=au_frq5, gamma=au_gam5, sigma=au_sig5)]

au = mp.Medium(epsilon=1.0, E_susceptibilities=au_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# copper (Cu)

metal_range = mp.FreqRange(min=um_scale/12.398, max=um_scale/.20664)

cu_plasma_frq = 10.83*e_v_um_scale
cu_f0 = 0.575
cu_frq0 = 1e-10
cu_gam0 = 0.030*e_v_um_scale
cu_sig0 = cu_f0*cu_plasma_frq**2/cu_frq0**2
cu_f1 = 0.061
cu_frq1 = 0.291*e_v_um_scale      # 4.261 um
cu_gam1 = 0.378*e_v_um_scale
cu_sig1 = cu_f1*cu_plasma_frq**2/cu_frq1**2
cu_f2 = 0.104
cu_frq2 = 2.957*e_v_um_scale      # 0.419 um
cu_gam2 = 1.056*e_v_um_scale
cu_sig2 = cu_f2*cu_plasma_frq**2/cu_frq2**2
cu_f3 = 0.723
cu_frq3 = 5.300*e_v_um_scale      # 0.234 um
cu_gam3 = 3.213*e_v_um_scale
cu_sig3 = cu_f3*cu_plasma_frq**2/cu_frq3**2
cu_f4 = 0.638
cu_frq4 = 11.18*e_v_um_scale      # 0.111 um
cu_gam4 = 4.305*e_v_um_scale
cu_sig4 = cu_f4*cu_plasma_frq**2/cu_frq4**2

cu_susc = [mp.DrudeSusceptibility(frequency=cu_frq0, gamma=cu_gam0, sigma=cu_sig0),
           mp.LorentzianSusceptibility(frequency=cu_frq1, gamma=cu_gam1, sigma=cu_sig1),
           mp.LorentzianSusceptibility(frequency=cu_frq2, gamma=cu_gam2, sigma=cu_sig2),
           mp.LorentzianSusceptibility(frequency=cu_frq3, gamma=cu_gam3, sigma=cu_sig3),
           mp.LorentzianSusceptibility(frequency=cu_frq4, gamma=cu_gam4, sigma=cu_sig4)]

cu = mp.Medium(epsilon=1.0, E_susceptibilities=cu_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# aluminum (Al)

al_plasma_frq = 14.98*e_v_um_scale
al_f0 = 0.523
al_frq0 = 1e-10
al_gam0 = 0.047*e_v_um_scale
al_sig0 = al_f0*al_plasma_frq**2/al_frq0**2
al_f1 = 0.227
al_frq1 = 0.162*e_v_um_scale      # 7.654 um
al_gam1 = 0.333*e_v_um_scale
al_sig1 = al_f1*al_plasma_frq**2/al_frq1**2
al_f2 = 0.050
al_frq2 = 1.544*e_v_um_scale      # 0.803 um
al_gam2 = 0.312*e_v_um_scale
al_sig2 = al_f2*al_plasma_frq**2/al_frq2**2
al_f3 = 0.166
al_frq3 = 1.808*e_v_um_scale      # 0.686 um
al_gam3 = 1.351*e_v_um_scale
al_sig3 = al_f3*al_plasma_frq**2/al_frq3**2
al_f4 = 0.030
al_frq4 = 3.473*e_v_um_scale      # 0.357 um
al_gam4 = 3.382*e_v_um_scale
al_sig4 = al_f4*al_plasma_frq**2/al_frq4**2

al_susc = [mp.DrudeSusceptibility(frequency=al_frq0, gamma=al_gam0, sigma=al_sig0),
           mp.LorentzianSusceptibility(frequency=al_frq1, gamma=al_gam1, sigma=al_sig1),
           mp.LorentzianSusceptibility(frequency=al_frq2, gamma=al_gam2, sigma=al_sig2),
           mp.LorentzianSusceptibility(frequency=al_frq3, gamma=al_gam3, sigma=al_sig3),
           mp.LorentzianSusceptibility(frequency=al_frq4, gamma=al_gam4, sigma=al_sig4)]

al = mp.Medium(epsilon=1.0, E_susceptibilities=al_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# beryllium (Be)

be_plasma_frq = 18.51*e_v_um_scale
be_f0 = 0.084
be_frq0 = 1e-10
be_gam0 = 0.035*e_v_um_scale
be_sig0 = be_f0*be_plasma_frq**2/be_frq0**2
be_f1 = 0.031
be_frq1 = 0.100*e_v_um_scale     # 12.398 um
be_gam1 = 1.664*e_v_um_scale
be_sig1 = be_f1*be_plasma_frq**2/be_frq1**2
be_f2 = 0.140
be_frq2 = 1.032*e_v_um_scale      # 1.201 um
be_gam2 = 3.395*e_v_um_scale
be_sig2 = be_f2*be_plasma_frq**2/be_frq2**2
be_f3 = 0.530
be_frq3 = 3.183*e_v_um_scale      # 0.390 um
be_gam3 = 4.454*e_v_um_scale
be_sig3 = be_f3*be_plasma_frq**2/be_frq3**2
be_f4 = 0.130
be_frq4 = 4.604*e_v_um_scale      # 0.269 um
be_gam4 = 1.802*e_v_um_scale
be_sig4 = be_f4*be_plasma_frq**2/be_frq4**2

be_susc = [mp.DrudeSusceptibility(frequency=be_frq0, gamma=be_gam0, sigma=be_sig0),
           mp.LorentzianSusceptibility(frequency=be_frq1, gamma=be_gam1, sigma=be_sig1),
           mp.LorentzianSusceptibility(frequency=be_frq2, gamma=be_gam2, sigma=be_sig2),
           mp.LorentzianSusceptibility(frequency=be_frq3, gamma=be_gam3, sigma=be_sig3),
           mp.LorentzianSusceptibility(frequency=be_frq4, gamma=be_gam4, sigma=be_sig4)]

be = mp.Medium(epsilon=1.0, E_susceptibilities=be_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# chromium (Cr)

cr_plasma_frq = 10.75*e_v_um_scale
cr_f0 = 0.168
cr_frq0 = 1e-10
cr_gam0 = 0.047*e_v_um_scale
cr_sig0 = cr_f0*cr_plasma_frq**2/cr_frq0**2
cr_f1 = 0.151
cr_frq1 = 0.121*e_v_um_scale     # 10.247 um
cr_gam1 = 3.175*e_v_um_scale
cr_sig1 = cr_f1*cr_plasma_frq**2/cr_frq1**2
cr_f2 = 0.150
cr_frq2 = 0.543*e_v_um_scale      # 2.283 um
cr_gam2 = 1.305*e_v_um_scale
cr_sig2 = cr_f2*cr_plasma_frq**2/cr_frq2**2
cr_f3 = 1.149
cr_frq3 = 1.970*e_v_um_scale      # 0.629 um
cr_gam3 = 2.676*e_v_um_scale
cr_sig3 = cr_f3*cr_plasma_frq**2/cr_frq3**2
cr_f4 = 0.825
cr_frq4 = 8.775*e_v_um_scale      # 0.141 um
cr_gam4 = 1.335*e_v_um_scale
cr_sig4 = cr_f4*cr_plasma_frq**2/cr_frq4**2

cr_susc = [mp.DrudeSusceptibility(frequency=cr_frq0, gamma=cr_gam0, sigma=cr_sig0),
           mp.LorentzianSusceptibility(frequency=cr_frq1, gamma=cr_gam1, sigma=cr_sig1),
           mp.LorentzianSusceptibility(frequency=cr_frq2, gamma=cr_gam2, sigma=cr_sig2),
           mp.LorentzianSusceptibility(frequency=cr_frq3, gamma=cr_gam3, sigma=cr_sig3),
           mp.LorentzianSusceptibility(frequency=cr_frq4, gamma=cr_gam4, sigma=cr_sig4)]

cr = mp.Medium(epsilon=1.0, E_susceptibilities=cr_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# nickel (Ni)

ni_plasma_frq = 15.92*e_v_um_scale
ni_f0 = 0.096
ni_frq0 = 1e-10
ni_gam0 = 0.048*e_v_um_scale
ni_sig0 = ni_f0*ni_plasma_frq**2/ni_frq0**2
ni_f1 = 0.100
ni_frq1 = 0.174*e_v_um_scale      # 7.126 um
ni_gam1 = 4.511*e_v_um_scale
ni_sig1 = ni_f1*ni_plasma_frq**2/ni_frq1**2
ni_f2 = 0.135
ni_frq2 = 0.582*e_v_um_scale      # 2.130 um
ni_gam2 = 1.334*e_v_um_scale
ni_sig2 = ni_f2*ni_plasma_frq**2/ni_frq2**2
ni_f3 = 0.106
ni_frq3 = 1.597*e_v_um_scale      # 0.776 um
ni_gam3 = 2.178*e_v_um_scale
ni_sig3 = ni_f3*ni_plasma_frq**2/ni_frq3**2
ni_f4 = 0.729
ni_frq4 = 6.089*e_v_um_scale      # 0.204 um
ni_gam4 = 6.292*e_v_um_scale
ni_sig4 = ni_f4*ni_plasma_frq**2/ni_frq4**2

ni_susc = [mp.DrudeSusceptibility(frequency=ni_frq0, gamma=ni_gam0, sigma=ni_sig0),
           mp.LorentzianSusceptibility(frequency=ni_frq1, gamma=ni_gam1, sigma=ni_sig1),
           mp.LorentzianSusceptibility(frequency=ni_frq2, gamma=ni_gam2, sigma=ni_sig2),
           mp.LorentzianSusceptibility(frequency=ni_frq3, gamma=ni_gam3, sigma=ni_sig3),
           mp.LorentzianSusceptibility(frequency=ni_frq4, gamma=ni_gam4, sigma=ni_sig4)]

ni = mp.Medium(epsilon=1.0, E_susceptibilities=ni_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# palladium (Pd)

pd_plasma_frq = 9.72*e_v_um_scale
pd_f0 = 0.330
pd_frq0 = 1e-10
pd_gam0 = 0.008*e_v_um_scale
pd_sig0 = pd_f0*pd_plasma_frq**2/pd_frq0**2
pd_f1 = 0.649
pd_frq1 = 0.336*e_v_um_scale      # 3.690 um
pd_gam1 = 2.950*e_v_um_scale
pd_sig1 = pd_f1*pd_plasma_frq**2/pd_frq1**2
pd_f2 = 0.121
pd_frq2 = 0.501*e_v_um_scale      # 2.475 um
pd_gam2 = 0.555*e_v_um_scale
pd_sig2 = pd_f2*pd_plasma_frq**2/pd_frq2**2
pd_f3 = 0.638
pd_frq3 = 1.659*e_v_um_scale      # 0.747 um
pd_gam3 = 4.621*e_v_um_scale
pd_sig3 = pd_f3*pd_plasma_frq**2/pd_frq3**2
pd_f4 = 0.453
pd_frq4 = 5.715*e_v_um_scale      # 0.217 um
pd_gam4 = 3.236*e_v_um_scale
pd_sig4 = pd_f4*pd_plasma_frq**2/pd_frq4**2

pd_susc = [mp.DrudeSusceptibility(frequency=pd_frq0, gamma=pd_gam0, sigma=pd_sig0),
           mp.LorentzianSusceptibility(frequency=pd_frq1, gamma=pd_gam1, sigma=pd_sig1),
           mp.LorentzianSusceptibility(frequency=pd_frq2, gamma=pd_gam2, sigma=pd_sig2),
           mp.LorentzianSusceptibility(frequency=pd_frq3, gamma=pd_gam3, sigma=pd_sig3),
           mp.LorentzianSusceptibility(frequency=pd_frq4, gamma=pd_gam4, sigma=pd_sig4)]

pd = mp.Medium(epsilon=1.0, E_susceptibilities=pd_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# platinum (Pt)

pt_plasma_frq = 9.59*e_v_um_scale
pt_f0 = 0.333
pt_frq0 = 1e-10
pt_gam0 = 0.080*e_v_um_scale
pt_sig0 = pt_f0*pt_plasma_frq**2/pt_frq0**2
pt_f1 = 0.191
pt_frq1 = 0.780*e_v_um_scale      # 1.590 um
pt_gam1 = 0.517*e_v_um_scale
pt_sig1 = pt_f1*pt_plasma_frq**2/pt_frq1**2
pt_f2 = 0.659
pt_frq2 = 1.314*e_v_um_scale      # 0.944 um
pt_gam2 = 1.838*e_v_um_scale
pt_sig2 = pt_f2*pt_plasma_frq**2/pt_frq2**2
pt_f3 = 0.547
pt_frq3 = 3.141*e_v_um_scale      # 0.395 um
pt_gam3 = 3.668*e_v_um_scale
pt_sig3 = pt_f3*pt_plasma_frq**2/pt_frq3**2
pt_f4 = 3.576
pt_frq4 = 9.249*e_v_um_scale      # 0.134 um
pt_gam4 = 8.517*e_v_um_scale
pt_sig4 = pt_f4*pt_plasma_frq**2/pt_frq4**2

pt_susc = [mp.DrudeSusceptibility(frequency=pt_frq0, gamma=pt_gam0, sigma=pt_sig0),
           mp.LorentzianSusceptibility(frequency=pt_frq1, gamma=pt_gam1, sigma=pt_sig1),
           mp.LorentzianSusceptibility(frequency=pt_frq2, gamma=pt_gam2, sigma=pt_sig2),
           mp.LorentzianSusceptibility(frequency=pt_frq3, gamma=pt_gam3, sigma=pt_sig3),
           mp.LorentzianSusceptibility(frequency=pt_frq4, gamma=pt_gam4, sigma=pt_sig4)]

pt = mp.Medium(epsilon=1.0, E_susceptibilities=pt_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# titanium (Ti)

ti_plasma_frq = 7.29*e_v_um_scale
ti_f0 = 0.148
ti_frq0 = 1e-10
ti_gam0 = 0.082*e_v_um_scale
ti_sig0 = ti_f0*ti_plasma_frq**2/ti_frq0**2
ti_f1 = 0.899
ti_frq1 = 0.777*e_v_um_scale      # 1.596 um
ti_gam1 = 2.276*e_v_um_scale
ti_sig1 = ti_f1*ti_plasma_frq**2/ti_frq1**2
ti_f2 = 0.393
ti_frq2 = 1.545*e_v_um_scale      # 0.802 um
ti_gam2 = 2.518*e_v_um_scale
ti_sig2 = ti_f2*ti_plasma_frq**2/ti_frq2**2
ti_f3 = 0.187
ti_frq3 = 2.509*e_v_um_scale      # 0.494 um
ti_gam3 = 1.663*e_v_um_scale
ti_sig3 = ti_f3*ti_plasma_frq**2/ti_frq3**2
ti_f4 = 0.001
ti_frq4 = 19.43*e_v_um_scale      # 0.064 um
ti_gam4 = 1.762*e_v_um_scale
ti_sig4 = ti_f4*ti_plasma_frq**2/ti_frq4**2

ti_susc = [mp.DrudeSusceptibility(frequency=ti_frq0, gamma=ti_gam0, sigma=ti_sig0),
           mp.LorentzianSusceptibility(frequency=ti_frq1, gamma=ti_gam1, sigma=ti_sig1),
           mp.LorentzianSusceptibility(frequency=ti_frq2, gamma=ti_gam2, sigma=ti_sig2),
           mp.LorentzianSusceptibility(frequency=ti_frq3, gamma=ti_gam3, sigma=ti_sig3),
           mp.LorentzianSusceptibility(frequency=ti_frq4, gamma=ti_gam4, sigma=ti_sig4)]

ti = mp.Medium(epsilon=1.0, E_susceptibilities=ti_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# tungsten (W)

w_plasma_frq = 13.22*e_v_um_scale
w_f0 = 0.206
w_frq0 = 1e-10
w_gam0 = 0.064*e_v_um_scale
w_sig0 = w_f0*w_plasma_frq**2/w_frq0**2
w_f1 = 0.054
w_frq1 = 1.004*e_v_um_scale      # 1.235 um
w_gam1 = 0.530*e_v_um_scale
w_sig1 = w_f1*w_plasma_frq**2/w_frq1**2
w_f2 = 0.166
w_frq2 = 1.917*e_v_um_scale      # 0.647 um
w_gam2 = 1.281*e_v_um_scale
w_sig2 = w_f2*w_plasma_frq**2/w_frq2**2
w_f3 = 0.706
w_frq3 = 3.580*e_v_um_scale      # 0.346 um
w_gam3 = 3.332*e_v_um_scale
w_sig3 = w_f3*w_plasma_frq**2/w_frq3**2
w_f4 = 2.590
w_frq4 = 7.498*e_v_um_scale      # 0.165 um
w_gam4 = 5.836*e_v_um_scale
w_sig4 = w_f4*w_plasma_frq**2/w_frq4**2

w_susc = [mp.DrudeSusceptibility(frequency=w_frq0, gamma=w_gam0, sigma=w_sig0),
          mp.LorentzianSusceptibility(frequency=w_frq1, gamma=w_gam1, sigma=w_sig1),
          mp.LorentzianSusceptibility(frequency=w_frq2, gamma=w_gam2, sigma=w_sig2),
          mp.LorentzianSusceptibility(frequency=w_frq3, gamma=w_gam3, sigma=w_sig3),
          mp.LorentzianSusceptibility(frequency=w_frq4, gamma=w_gam4, sigma=w_sig4)]

w = mp.Medium(epsilon=1.0, E_susceptibilities=w_susc, valid_freq_range=metal_range)

#------------------------------------------------------------------
# metals from D. Barchiesi and T. Grosges, J. Nanophotonics, Vol. 8, 08996, 2015
# wavelength range: 0.4 - 0.8 um

metal_visible_range = mp.FreqRange(min=um_scale/0.8, max=um_scale/0.4)

# gold (Au)
# fit to P.B. Johnson and R.W. Christy, Physical Review B, Vol. 6, pp. 4370-9, 1972

au_jc_visible_frq0 = 1/(0.139779231751333*um_scale)
au_jc_visible_gam0 = 1/(26.1269913352870*um_scale)
au_jc_visible_sig0 = 1

au_jc_visible_frq1 = 1/(0.404064525036786*um_scale)
au_jc_visible_gam1 = 1/(1.12834046202759*um_scale)
au_jc_visible_sig1 = 2.07118534879440

au_jc_visible_susc = [mp.DrudeSusceptibility(frequency=au_jc_visible_frq0, gamma=au_jc_visible_gam0, sigma=au_jc_visible_sig0),
                      mp.LorentzianSusceptibility(frequency=au_jc_visible_frq1, gamma=au_jc_visible_gam1, sigma=au_jc_visible_sig1)]

au_jc_visible = mp.Medium(epsilon=6.1599, E_susceptibilities=au_jc_visible_susc)

#------------------------------------------------------------------
# gold (Au)
# fit to E.D. Palik, Handbook of Optical Constants, Academic Press, 1985 

au_visible_frq0 = 1/(0.0473629248511456*um_scale)
au_visible_gam0 = 1/(0.255476199605166*um_scale)
au_visible_sig0 = 1

au_visible_frq1 = 1/(0.800619321082804*um_scale)
au_visible_gam1 = 1/(0.381870287531951*um_scale)
au_visible_sig1 = -169.060953137985

au_visible_susc = [mp.DrudeSusceptibility(frequency=au_visible_frq0, gamma=au_visible_gam0, sigma=au_visible_sig0),
                   mp.LorentzianSusceptibility(frequency=au_visible_frq1, gamma=au_visible_gam1, sigma=au_visible_sig1)]

au_visible = mp.Medium(epsilon=0.6888, E_susceptibilities=au_visible_susc, valid_freq_range=metal_visible_range)

#------------------------------------------------------------------
## WARNING: unstable; field divergence may occur

# silver (Au)
# fit to E.D. Palik, Handbook of Optical Constants, Academic Press, 1985 

ag_visible_frq0 = 1/(0.142050162130618*um_scale)
ag_visible_gam0 = 1/(18.0357292925015*um_scale)
ag_visible_sig0 = 1

ag_visible_frq1 = 1/(0.115692151792108*um_scale)
ag_visible_gam1 = 1/(0.257794324096575*um_scale)
ag_visible_sig1 = 3.74465275944019

ag_visible_susc = [mp.DrudeSusceptibility(frequency=ag_visible_frq0, gamma=ag_visible_gam0, sigma=ag_visible_sig0),
                   mp.LorentzianSusceptibility(frequency=ag_visible_frq1, gamma=ag_visible_gam1, sigma=ag_visible_sig1)]

ag_visible = mp.Medium(epsilon=0.0067526, E_susceptibilities=ag_visible_susc, valid_freq_range=metal_visible_range)

#------------------------------------------------------------------
## WARNING: unstable; field divergence may occur

# aluminum (Al)
# fit to E.D. Palik, Handbook of Optical Constants, Academic Press, 1985 

al_visible_frq0 = 1/(0.0625841659042985*um_scale)
al_visible_gam0 = 1/(0.606007002962666*um_scale)
al_visible_sig0 = 1

al_visible_frq1 = 1/(0.528191199577075*um_scale)
al_visible_gam1 = 1/(0.291862527666814*um_scale)
al_visible_sig1 = -44.4456675577921

al_visible_susc = [mp.DrudeSusceptibility(frequency=al_visible_frq0, gamma=al_visible_gam0, sigma=al_visible_sig0),
                   mp.LorentzianSusceptibility(frequency=al_visible_frq1, gamma=al_visible_gam1, sigma=al_visible_sig1)]

al_visible = mp.Medium(epsilon=0.13313, E_susceptibilities=al_visible_susc, valid_freq_range=metal_visible_range)

#------------------------------------------------------------------
# chroimium (Cr)
# fit to E.D. Palik, Handbook of Optical Constants, Academic Press, 1985 

cr_visible_frq0 = 1/(0.118410119507342*um_scale)
cr_visible_gam0 = 1/(0.628596264869804*um_scale)
cr_visible_sig0 = 1

cr_visible_frq1 = 1/(0.565709598452496*um_scale)
cr_visible_gam1 = 1/(0.731117670900812*um_scale)
cr_visible_sig1 = 13.2912419951294

cr_visible_susc = [mp.DrudeSusceptibility(frequency=cr_visible_frq0, gamma=cr_visible_gam0, sigma=cr_visible_sig0),
                   mp.LorentzianSusceptibility(frequency=cr_visible_frq1, gamma=cr_visible_gam1, sigma=cr_visible_sig1)]

cr_visible = mp.Medium(epsilon=2.7767, E_susceptibilities=cr_visible_susc, valid_freq_range=metal_visible_range)

#------------------------------------------------------------------
## WARNING: unstable; field divergence may occur

# titanium (Ti)
# fit to E.D. Palik, Handbook of Optical Constants, Academic Press, 1985 

ti_visible_frq0 = 1/(0.101331651921602*um_scale)
ti_visible_gam0 = 1/(0.365743382258719*um_scale)
ti_visible_sig0 = 1

ti_visible_frq1 = 1/(4.56839173979216e-09*um_scale)
ti_visible_gam1 = 1/(5.86441957443603e-10*um_scale)
ti_visible_sig1 = 54742662.1963414

ti_visible_susc = [mp.DrudeSusceptibility(frequency=ti_visible_frq0, gamma=ti_visible_gam0, sigma=ti_visible_sig0),
                   mp.LorentzianSusceptibility(frequency=ti_visible_frq1, gamma=ti_visible_gam1, sigma=ti_visible_sig1)]

ti_visible = mp.Medium(epsilon=-5.4742e7, E_susceptibilities=ti_visible_susc, valid_freq_range=metal_visible_range)

#------------------------------------------------------------------
# aluminum (Al) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.19 - 0.83 um

al_drude_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.19)

al_drude_frq = 1/(0.0789607648707171*um_scale)
al_drude_gam = 1/(1.78138208333333*um_scale)
al_drude_sig = 1

al_drude_susc = [mp.DrudeSusceptibility(frequency=al_drude_frq, gamma=al_drude_gam, sigma=al_drude_sig)]

al_drude = mp.Medium(epsilon=1.0, E_susceptibilities=al_drude_susc, valid_freq_range=al_drude_range)

#------------------------------------------------------------------
# cobalt (Co) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.26 - 1.65 um

co_range = mp.FreqRange(min=um_scale/1.65, max=um_scale/0.26)

co_frq = 1/(0.0789607648707171*um_scale)
co_gam = 1/(0.213802712536644*um_scale)
co_sig = 1

co_susc = [mp.DrudeSusceptibility(frequency=co_frq, gamma=co_gam, sigma=co_sig)]

co = mp.Medium(epsilon=3.694, E_susceptibilities=co_susc, valid_freq_range=co_range)

#------------------------------------------------------------------
## WARNING: unstable; field divergence may occur

# molybdenum (Mo) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.25 - 0.83 um

mo_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.25)

mo_frq = 1/(0.0620790071099539*um_scale)
mo_gam = 1/(0.148359690080172*um_scale)
mo_sig = 1

mo_susc = [mp.DrudeSusceptibility(frequency=mo_frq, gamma=mo_gam, sigma=mo_sig)]

mo = mp.Medium(epsilon=-1.366, E_susceptibilities=mo_susc, valid_freq_range=mo_range)

#------------------------------------------------------------------
# nickel chrome (NiCr) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.25 - 0.83 um

ni_cr_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.25)

ni_cr_frq = 1/(0.0868845080588648*um_scale)
ni_cr_gam = 1/(0.308418390547264*um_scale)
ni_cr_sig = 1

ni_cr_susc = [ mp.DrudeSusceptibility(frequency=ni_cr_frq, gamma=ni_cr_gam, sigma=ni_cr_sig) ]

ni_cr = mp.Medium(epsilon=1.0, E_susceptibilities=ni_cr_susc, valid_freq_range=ni_cr_range)

#------------------------------------------------------------------
# nickel iron (NiFe) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.25 - 0.83 um

ni_fe_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.25)

ni_fe_frq = 1/(0.0838297450980392*um_scale)
ni_fe_gam = 1/(0.259381156903766*um_scale)
ni_fe_sig = 1

ni_fe_susc = [mp.DrudeSusceptibility(frequency=ni_fe_frq, gamma=ni_fe_gam, sigma=ni_fe_sig)]

ni_fe = mp.Medium(epsilon=1.0, E_susceptibilities=ni_fe_susc, valid_freq_range=ni_fe_range)

#------------------------------------------------------------------
# titanium (Ti) from Horiba Technical Note 09: Drude Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Drude_Dispersion_Model.pdf
# wavelength range: 0.21 - 1.24 um

ti_drude_range = mp.FreqRange(min=um_scale/1.24, max=um_scale/0.21)

ti_drude_frq = 1/(0.113746966055046*um_scale)
ti_drude_gam = 1/(0.490056098814229*um_scale)
ti_drude_sig = 1

ti_drude_susc = [mp.DrudeSusceptibility(frequency=ti_drude_frq, gamma=ti_drude_gam, sigma=ti_drude_sig)]

ti_drude = mp.Medium(epsilon=1.0, E_susceptibilities=ti_drude_susc, valid_freq_range=ti_drude_range)

#------------------------------------------------------------------
# silicon nitride (SiN), non-stoichiometric, from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.21 - 2.07 um

si_n_range = mp.FreqRange(min=um_scale/2.07, max=um_scale/0.21)

si_n_frq1 = 1/(0.190891752117013*um_scale)
si_n_gam1 = 1/(3.11518072864322*um_scale)
si_n_sig1 = 1.2650

si_n_susc = [mp.LorentzianSusceptibility(frequency=si_n_frq1, gamma=si_n_gam1, sigma=si_n_sig1)]

si_n = mp.Medium(epsilon=2.320, E_susceptibilities=si_n_susc, valid_freq_range=si_n_range)

#------------------------------------------------------------------
# silicon nitride (Si3N4), stoichiometric, from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.23 - 0.83 um

si3_n4_range = mp.FreqRange(min=um_scale/0.83, max=um_scale/0.23)

si3_n4_frq1 = 1/(0.389153148148148*um_scale)
si3_n4_gam1 = 1/(0.693811936205932*um_scale)
si3_n4_sig1 = 4.377

si3_n4_susc = [mp.LorentzianSusceptibility(frequency=si3_n4_frq1, gamma=si3_n4_gam1, sigma=si3_n4_sig1)]

si3_n4 = mp.Medium(epsilon=1.0, E_susceptibilities=si3_n4_susc, valid_freq_range=si3_n4_range)

#------------------------------------------------------------------
# silicon dioxide (SiO2) from Horiba Technical Note 08: Lorentz Dispersion Model
# ref: http://www.horiba.com/fileadmin/uploads/Scientific/Downloads/OpticalSchool_CN/TN/ellipsometer/Lorentz_Dispersion_Model.pdf
# wavelength range: 0.25 - 1.77 um

si_o2_range = mp.FreqRange(min=um_scale/1.77, max=um_scale/0.25)

si_o2_frq1 = 1/(0.103320160833333*um_scale)
si_o2_gam1 = 1/(12.3984193000000*um_scale)
si_o2_sig1 = 1.12

si_o2_susc = [mp.LorentzianSusceptibility(frequency=si_o2_frq1, gamma=si_o2_gam1, sigma=si_o2_sig1)]

si_o2 = mp.Medium(epsilon=1.0, E_susceptibilities=si_o2_susc, valid_freq_range=si_o2_range)

#------------------------------------------------------------------
# indium phosphide (InP) from Handbook of Optics, 2nd edition, Vol. 2, McGraw-Hill, 1994
# ref: https://refractiveindex.info/?shelf=main&book=InP&page=Pettit
# wavelength range: 0.95 - 10 um

in_p_range = mp.FreqRange(min=um_scale/10, max=um_scale/0.95)

in_p_frq1 = 1/(0.6263*um_scale)
in_p_gam1 = 0
in_p_sig1 = 2.316
in_p_frq2 = 1/(32.935*um_scale)
in_p_gam2 = 0
in_p_sig2 = 2.765

in_p_susc = [mp.LorentzianSusceptibility(frequency=in_p_frq1, gamma=in_p_gam1, sigma=in_p_sig1),
            mp.LorentzianSusceptibility(frequency=in_p_frq2, gamma=in_p_gam2, sigma=in_p_sig2)]

in_p = mp.Medium(epsilon=7.255, E_susceptibilities=in_p_susc, valid_freq_range=in_p_range)

#------------------------------------------------------------------
# germanium (Ge) from N. P. Barnes and M. S. Piltch, J. Optical Society America, Vol. 69, pp. 178-180, 1979
# ref: https://refractiveindex.info/?shelf=main&book=Ge&page=Icenogle
# wavelength range: 2.5 - 12 um

ge_range = mp.FreqRange(min=um_scale/12, max=um_scale/2.5)

ge_frq1 = 1/(0.6641159*um_scale)
ge_gam1 = 0
ge_sig1 = 6.7288
ge_frq2 = 1/(62.210127*um_scale)
ge_gam2 = 0
ge_sig2 = 0.21307

ge_susc = [mp.LorentzianSusceptibility(frequency=ge_frq1, gamma=ge_gam1, sigma=ge_sig1),
           mp.LorentzianSusceptibility(frequency=ge_frq2, gamma=ge_gam2, sigma=ge_sig2)]

ge = mp.Medium(epsilon=9.28156, E_susceptibilities=ge_susc, valid_freq_range=ge_range)

#------------------------------------------------------------------
# silicon (Si) from C. D. Salzberg and J. J. Villa, , J. Optical Society America, Vol. 47, pp. 244-246, 1957
# ref: https://refractiveindex.info/?shelf=main&book=Si&page=Salzberg
# wavelength range: 1.36 - 11 um

si_range = mp.FreqRange(min=um_scale/11, max=um_scale/1.36)

si_frq1 = 1/(0.301516485*um_scale)
si_gam1 = 0
si_sig1 = 10.6684293
si_frq2 = 1/(1.13475115*um_scale)
si_gam2 = 0
si_sig2 = 0.0030434748
si_frq3 = 1/(1104*um_scale)
si_gam3 = 0
si_sig3 = 1.54133408

si_susc = [mp.LorentzianSusceptibility(frequency=si_frq1, gamma=si_gam1, sigma=si_sig1),
           mp.LorentzianSusceptibility(frequency=si_frq2, gamma=si_gam2, sigma=si_sig2),
           mp.LorentzianSusceptibility(frequency=si_frq3, gamma=si_gam3, sigma=si_sig3)]

si = mp.Medium(epsilon=1.0, E_susceptibilities=si_susc, valid_freq_range=si_range)

#------------------------------------------------------------------
# poly(methyl methacrylate) (PMMA) from N. Sultanova et al., Acta Physica Polonica A, Vol. 116, pp. 585-7, 2009
# ref: https://refractiveindex.info/?shelf=organic&book=poly%28methyl_methacrylate%29&page=Sultanova
# wavelength range: 0.437 - 1.052 um

pmma_range = mp.FreqRange(min=um_scale/1.052, max=um_scale/0.437)

pmma_frq1 = 1/(0.106362587407415*um_scale)
pmma_gam1 = 0
pmma_sig1 = 1.1819

pmma_susc = [mp.LorentzianSusceptibility(frequency=pmma_frq1, gamma=pmma_gam1, sigma=pmma_sig1)]

pmma = mp.Medium(epsilon=1.0, E_susceptibilities=pmma_susc, valid_freq_range=pmma_range)

#------------------------------------------------------------------
# polycarbonate (PC) from N. Sultanova et al., Acta Physica Polonica A, Vol. 116, pp. 585-7, 2009
# ref: https://refractiveindex.info/?shelf=organic&book=polycarbonate&page=Sultanova
# wavelength range: 0.437 - 1.052 um

pc_range = mp.FreqRange(min=um_scale/1.052, max=um_scale/0.437)

pc_frq1 = 1/(0.145958898324152*um_scale)
pc_gam1 = 0
pc_sig1 = 1.4182

pc_susc = [mp.LorentzianSusceptibility(frequency=pc_frq1, gamma=pc_gam1, sigma=pc_sig1)]

pc = mp.Medium(epsilon=1.0, E_susceptibilities=pc_susc, valid_freq_range=pc_range)

#------------------------------------------------------------------
# polystyrene (PS) from N. Sultanova et al., Acta Physica Polonica A, Vol. 116, pp. 585-7, 2009
# ref: https://refractiveindex.info/?shelf=organic&book=polystyren&page=Sultanova
# wavelength range: 0.437 - 1.052 um

ps_range = mp.FreqRange(min=um_scale/1.052, max=um_scale/0.437)

ps_frq1 = 1/(0.142182980697410*um_scale)
ps_gam1 = 0
ps_sig1 = 1.4435

ps_susc = [mp.LorentzianSusceptibility(frequency=ps_frq1, gamma=ps_gam1, sigma=ps_sig1)]

ps = mp.Medium(epsilon=1.0, E_susceptibilities=ps_susc, valid_freq_range=ps_range)

#------------------------------------------------------------------
# cellulose (CLS) from N. Sultanova et al., Acta Physica Polonica A, Vol. 116, pp. 585-7, 2009
# ref: https://refractiveindex.info/?shelf=organic&book=cellulose&page=Sultanova
# wavelength range: 0.437 - 1.052 um

cls_range = mp.FreqRange(min=um_scale/1.052, max=um_scale/0.437)

cls_frq1 = 1/(0.105294824184287*um_scale)
cls_gam1 = 0
cls_sig1 = 1.124

cls_susc = [mp.LorentzianSusceptibility(frequency=cls_frq1, gamma=cls_gam1, sigma=cls_sig1)]

cls = mp.Medium(epsilon=1.0, E_susceptibilities=cls_susc, valid_freq_range=cls_range)

#------------------------------------------------------------------
# barium borate (BaB2O4), beta phase, from G. Tamosauskas et al., Optical Materials Express, Vol. 8, pp. 1410-18, 2018
# ref: https://refractiveindex.info/?shelf=main&book=BaB2O4&page=Tamosauskas-o
# ref: https://refractiveindex.info/?shelf=main&book=BaB2O4&page=Tamosauskas-e
# wavelength range: 0.188 - 5.2 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

ba_b2_o4_range = mp.FreqRange(min=um_scale/5.2, max=um_scale/0.188)

ba_b2_o4_frq1 = 1/(0.06265780079128216*um_scale)
ba_b2_o4_gam1 = 0
ba_b2_o4_sig1 = 0.90291
ba_b2_o4_frq2 = 1/(0.13706202975295528*um_scale)
ba_b2_o4_gam2 = 0
ba_b2_o4_sig2 = 0.83155
ba_b2_o4_frq3 = 1/(7.746612162745725*um_scale)
ba_b2_o4_gam3 = 0
ba_b2_o4_sig3 = 0.76536

ba_b2_o4_susc_o = [mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq1, gamma=ba_b2_o4_gam1, sigma_diag=ba_b2_o4_sig1*mp.Vector3(1,1,0)),
                 mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq2, gamma=ba_b2_o4_gam2, sigma_diag=ba_b2_o4_sig2*mp.Vector3(1,1,0)),
                 mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq3, gamma=ba_b2_o4_gam3, sigma_diag=ba_b2_o4_sig3*mp.Vector3(1,1,0))]

ba_b2_o4_frq1 = 1/(0.0845103543951864*um_scale)
ba_b2_o4_gam1 = 0
ba_b2_o4_sig1 = 1.151075
ba_b2_o4_frq2 = 1/(0.15029970059850417*um_scale)
ba_b2_o4_gam2 = 0
ba_b2_o4_sig2 = 0.21803
ba_b2_o4_frq3 = 1/(16.217274740226856*um_scale)
ba_b2_o4_gam3 = 0
ba_b2_o4_sig3 = 0.656

ba_b2_o4_susc_e = [mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq1, gamma=ba_b2_o4_gam1, sigma_diag=ba_b2_o4_sig1*mp.Vector3(0,0,1)),
                 mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq2, gamma=ba_b2_o4_gam2, sigma_diag=ba_b2_o4_sig2*mp.Vector3(0,0,1)),
                 mp.LorentzianSusceptibility(frequency=ba_b2_o4_frq3, gamma=ba_b2_o4_gam3, sigma_diag=ba_b2_o4_sig3*mp.Vector3(0,0,1))]

ba_b2_o4 = mp.Medium(epsilon=1.0, E_susceptibilities=ba_b2_o4_susc_o+ba_b2_o4_susc_e, valid_freq_range=ba_b2_o4_range)

#------------------------------------------------------------------
# lithium niobate (LiNbO3) from D.E. Zelmon et al., J. Optical Society of America B, Vol. 14, pp. 3319-22, 1997
# ref: https://refractiveindex.info/?shelf=main&book=LiNbO3&page=Zelmon-o
# ref: https://refractiveindex.info/?shelf=main&book=LiNbO3&page=Zelmon-e
# wavelength range: 0.4 - 5.0 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

li_nb_o3_range = mp.FreqRange(min=um_scale/5.0, max=um_scale/0.4)

li_nb_o3_frq1 = 1/(0.13281566172707193*um_scale)
li_nb_o3_gam1 = 0
li_nb_o3_sig1 = 2.6734
li_nb_o3_frq2 = 1/(0.24318717071424636*um_scale)
li_nb_o3_gam2 = 0
li_nb_o3_sig2 = 1.2290
li_nb_o3_frq3 = 1/(21.78531615561271*um_scale)
li_nb_o3_gam3 = 0
li_nb_o3_sig3 = 12.614

li_nb_o3_susc_o = [mp.LorentzianSusceptibility(frequency=li_nb_o3_frq1, gamma=li_nb_o3_gam1, sigma_diag=li_nb_o3_sig1*mp.Vector3(1,1,0)),
                 mp.LorentzianSusceptibility(frequency=li_nb_o3_frq2, gamma=li_nb_o3_gam2, sigma_diag=li_nb_o3_sig2*mp.Vector3(1,1,0)),
                 mp.LorentzianSusceptibility(frequency=li_nb_o3_frq3, gamma=li_nb_o3_gam3, sigma_diag=li_nb_o3_sig3*mp.Vector3(1,1,0))]

li_nb_o3_frq1 = 1/(0.14307340773183533*um_scale)
li_nb_o3_gam1 = 0
li_nb_o3_sig1 = 2.9804
li_nb_o3_frq2 = 1/(0.2580697580112788*um_scale)
li_nb_o3_gam2 = 0
li_nb_o3_sig2 = 0.5981
li_nb_o3_frq3 = 1/(20.39803912144498*um_scale)
li_nb_o3_gam3 = 0
li_nb_o3_sig3 = 8.9543

li_nb_o3_susc_e = [mp.LorentzianSusceptibility(frequency=li_nb_o3_frq1, gamma=li_nb_o3_gam1, sigma_diag=li_nb_o3_sig1*mp.Vector3(0,0,1)),
                 mp.LorentzianSusceptibility(frequency=li_nb_o3_frq2, gamma=li_nb_o3_gam2, sigma_diag=li_nb_o3_sig2*mp.Vector3(0,0,1)),
                 mp.LorentzianSusceptibility(frequency=li_nb_o3_frq3, gamma=li_nb_o3_gam3, sigma_diag=li_nb_o3_sig3*mp.Vector3(0,0,1))]

li_nb_o3 = mp.Medium(epsilon=1.0, E_susceptibilities=li_nb_o3_susc_o+li_nb_o3_susc_e, valid_freq_range=li_nb_o3_range)

#------------------------------------------------------------------
# calcium tungstate (CaWO4) from W.L. Bond, J. Applied Physics, Vol. 36, pp. 1674-77, 1965
# ref: https://refractiveindex.info/?shelf=main&book=CaWO4&page=Bond-o
# ref: https://refractiveindex.info/?shelf=main&book=CaWO4&page=Bond-e
# wavelength range: 0.45 - 4.0 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

ca_wo4_range = mp.FreqRange(min=um_scale/4.0, max=um_scale/0.45)

ca_wo4_frq1 = 1/(0.1347*um_scale)
ca_wo4_gam1 = 0
ca_wo4_sig1 = 2.5493
ca_wo4_frq2 = 1/(10.815*um_scale)
ca_wo4_gam2 = 0
ca_wo4_sig2 = 0.9200

ca_wo4_susc_o = [mp.LorentzianSusceptibility(frequency=ca_wo4_frq1, gamma=ca_wo4_gam1, sigma_diag=ca_wo4_sig1*mp.Vector3(1,1,0)),
                mp.LorentzianSusceptibility(frequency=ca_wo4_frq2, gamma=ca_wo4_gam2, sigma_diag=ca_wo4_sig2*mp.Vector3(1,1,0))]

ca_wo4_frq1 = 1/(0.1379*um_scale)
ca_wo4_gam1 = 0
ca_wo4_sig1 = 2.6041
ca_wo4_frq2 = 1/(21.371*um_scale)
ca_wo4_gam2 = 0
ca_wo4_sig2 = 4.1237

ca_wo4_susc_e = [mp.LorentzianSusceptibility(frequency=ca_wo4_frq1, gamma=ca_wo4_gam1, sigma_diag=ca_wo4_sig1*mp.Vector3(0,0,1)),
                mp.LorentzianSusceptibility(frequency=ca_wo4_frq2, gamma=ca_wo4_gam2, sigma_diag=ca_wo4_sig2*mp.Vector3(0,0,1))]

ca_wo4 = mp.Medium(epsilon=1.0, E_susceptibilities=ca_wo4_susc_o+ca_wo4_susc_e, valid_freq_range=ca_wo4_range)

#------------------------------------------------------------------
# calcium carbonate (CaCO3) from G. Ghosh, Optics Communication, Vol. 163, pp. 95-102, 1999
# ref: https://refractiveindex.info/?shelf=main&book=CaCO3&page=Ghosh-o
# ref: https://refractiveindex.info/?shelf=main&book=CaCO3&page=Ghosh-e
# wavelength range: 0.204 - 2.172 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

ca_co3_range = mp.FreqRange(min=um_scale/2.172, max=um_scale/0.204)

ca_co3_frq1 = 1/(0.13940057496294625*um_scale)
ca_co3_gam1 = 0
ca_co3_sig1 = 0.96464345
ca_co3_frq2 = 1/(10.954451150103322*um_scale)
ca_co3_gam2 = 0
ca_co3_sig2 = 1.82831454

ca_co3_susc_o = [mp.LorentzianSusceptibility(frequency=ca_co3_frq1, gamma=ca_co3_gam1, sigma_diag=ca_co3_sig1*mp.Vector3(1,1,0)),
                mp.LorentzianSusceptibility(frequency=ca_co3_frq2, gamma=ca_co3_gam2, sigma_diag=ca_co3_sig2*mp.Vector3(1,1,0))]

ca_co3_frq1 = 1/(0.1032906302623815*um_scale)
ca_co3_gam1 = 0
ca_co3_sig1 = 0.82427830
ca_co3_frq2 = 1/(10.954451150103322*um_scale)
ca_co3_gam2 = 0
ca_co3_sig2 = 0.14429128

ca_co3_susc_e = [mp.LorentzianSusceptibility(frequency=ca_co3_frq1, gamma=ca_co3_gam1, sigma_diag=ca_co3_sig1*mp.Vector3(0,0,1)),
                mp.LorentzianSusceptibility(frequency=ca_co3_frq2, gamma=ca_co3_gam2, sigma_diag=ca_co3_sig2*mp.Vector3(0,0,1))]

ca_co3 = mp.Medium(epsilon_diag=mp.Vector3(1.73358749,1.73358749,1.35859695), E_susceptibilities=ca_co3_susc_o+ca_co3_susc_e, valid_freq_range=ca_co3_range)

#------------------------------------------------------------------
# silicon dioxide (SiO2) from G. Ghosh, Optics Communication, Vol. 163, pp. 95-102, 1999
# ref: https://refractiveindex.info/?shelf=main&book=SiO2&page=Ghosh-o
# ref: https://refractiveindex.info/?shelf=main&book=SiO2&page=Ghosh-e
# wavelength range: 0.198 - 2.0531 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

si_o2_range = mp.FreqRange(min=um_scale/2.0531, max=um_scale/0.198)

si_o2_frq1 = 1/(0.10029257051247614*um_scale)
si_o2_gam1 = 0
si_o2_sig1 = 1.07044083
si_o2_frq2 = 1/(10*um_scale)
si_o2_gam2 = 0
si_o2_sig2 = 1.10202242

si_o2_susc_o = [mp.LorentzianSusceptibility(frequency=si_o2_frq1, gamma=si_o2_gam1, sigma_diag=si_o2_sig1*mp.Vector3(1,1,0)),
               mp.LorentzianSusceptibility(frequency=si_o2_frq2, gamma=si_o2_gam2, sigma_diag=si_o2_sig2*mp.Vector3(1,1,0))]

si_o2_frq1 = 1/(0.10104546699382412*um_scale)
si_o2_gam1 = 0
si_o2_sig1 = 1.09509924
si_o2_frq2 = 1/(10*um_scale)
si_o2_gam2 = 0
si_o2_sig2 = 1.15662475

si_o2_susc_e = [mp.LorentzianSusceptibility(frequency=si_o2_frq1, gamma=si_o2_gam1, sigma_diag=si_o2_sig1*mp.Vector3(0,0,1)),
               mp.LorentzianSusceptibility(frequency=si_o2_frq2, gamma=si_o2_gam2, sigma_diag=si_o2_sig2*mp.Vector3(0,0,1))]

si_o2_aniso = mp.Medium(epsilon_diag=mp.Vector3(1.28604141,1.28604141,1.28851804), E_susceptibilities=si_o2_susc_o+si_o2_susc_e, valid_freq_range=si_o2_range)

#------------------------------------------------------------------
# gallium nitride (GaN), alpha phase (wurtzite), from A.S. Barker Jr. and M. Ilegems, Physical Review B, Vol. 7, pp. 743-50, 1973
# ref: https://refractiveindex.info/?shelf=main&book=GaN&page=Barker-o
# ref: https://refractiveindex.info/?shelf=main&book=GaN&page=Barker-e
# wavelength range: 0.35 - 10 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

ga_n_range = mp.FreqRange(min=um_scale/10.0, max=um_scale/0.35)

ga_n_frq1 = 1/(0.256*um_scale)
ga_n_gam1 = 0
ga_n_sig1 = 1.75
ga_n_frq2 = 1/(17.86*um_scale)
ga_n_gam2 = 0
ga_n_sig2 = 4.1

ga_n_susc_o = [mp.LorentzianSusceptibility(frequency=ga_n_frq1, gamma=ga_n_gam1, sigma_diag=ga_n_sig1*mp.Vector3(1,1,0)),
              mp.LorentzianSusceptibility(frequency=ga_n_frq2, gamma=ga_n_gam2, sigma_diag=ga_n_sig2*mp.Vector3(1,1,0))]

ga_n_frq1 = 1/(18.76*um_scale)
ga_n_gam1 = 0
ga_n_sig1 = 5.08

ga_n_susc_e = [mp.LorentzianSusceptibility(frequency=ga_n_frq1, gamma=ga_n_gam1, sigma_diag=ga_n_sig1*mp.Vector3(0,0,1))]

ga_n = mp.Medium(epsilon_diag=mp.Vector3(3.6,3.6,5.35), E_susceptibilities=ga_n_susc_o+ga_n_susc_e, valid_freq_range=ga_n_range)

#------------------------------------------------------------------
# aluminum nitride (AlN) from J. Pastrnak and L. Roskovcova, Physica Status Solidi, Vol. 14, K5-8, 1966
# ref: https://refractiveindex.info/?shelf=main&book=AlN&page=Pastrnak-o
# ref: https://refractiveindex.info/?shelf=main&book=AlN&page=Pastrnak-e
# wavelength range: 0.22 - 5 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

al_n_range = mp.FreqRange(min=um_scale/5.0, max=um_scale/0.22)

al_n_frq1 = 1/(0.1715*um_scale)
al_n_gam1 = 0
al_n_sig1 = 1.3786
al_n_frq2 = 1/(15.03*um_scale)
al_n_gam2 = 0
al_n_sig2 = 3.861

al_n_susc_o = [mp.LorentzianSusceptibility(frequency=al_n_frq1, gamma=al_n_gam1, sigma_diag=al_n_sig1*mp.Vector3(1,1,0)),
              mp.LorentzianSusceptibility(frequency=al_n_frq2, gamma=al_n_gam2, sigma_diag=al_n_sig2*mp.Vector3(1,1,0))]

al_n_frq1 = 1/(0.1746*um_scale)
al_n_gam1 = 0
al_n_sig1 = 1.6173
al_n_frq2 = 1/(15.03*um_scale)
al_n_gam2 = 0
al_n_sig2 = 4.139

al_n_susc_e = [mp.LorentzianSusceptibility(frequency=al_n_frq1, gamma=al_n_gam1, sigma_diag=al_n_sig1*mp.Vector3(0,0,1)),
              mp.LorentzianSusceptibility(frequency=al_n_frq2, gamma=al_n_gam2, sigma_diag=al_n_sig2*mp.Vector3(0,0,1))]

al_n_aniso = mp.Medium(epsilon_diag=mp.Vector3(3.1399,3.1399,3.0729), E_susceptibilities=al_n_susc_o+al_n_susc_e, valid_freq_range=al_n_range)

#------------------------------------------------------------------
# alumina/sapphire (Al2O3) from I.H. Malitson and M.J. Dodge, J. Optical Society of America, Vol. 62, pp. 1405, 1972
# ref: https://refractiveindex.info/?shelf=main&book=Al2O3&page=Malitson-o
# ref: https://refractiveindex.info/?shelf=main&book=Al2O3&page=Malitson-e
# wavelength range: 0.2 - 5 um

## NOTE: ordinary (o) axes in X and Y, extraordinary (e) axis in Z

al2_o3_range = mp.FreqRange(min=um_scale/5.0, max=um_scale/0.2)

al2_o3_frq1 = 1/(0.0726631*um_scale)
al2_o3_gam1 = 0
al2_o3_sig1 = 1.4313493
al2_o3_frq2 = 1/(0.1193242*um_scale)
al2_o3_gam2 = 0
al2_o3_sig2 = 0.65054713
al2_o3_frq3 = 1/(18.02825*um_scale)
al2_o3_gam3 = 0
al2_o3_sig3 = 5.3414021

al2_o3_susc_o = [mp.LorentzianSusceptibility(frequency=al2_o3_frq1, gamma=al2_o3_gam1, sigma_diag=al2_o3_sig1*mp.Vector3(1,1,0)),
                mp.LorentzianSusceptibility(frequency=al2_o3_frq2, gamma=al2_o3_gam2, sigma_diag=al2_o3_sig2*mp.Vector3(1,1,0)),
                mp.LorentzianSusceptibility(frequency=al2_o3_frq3, gamma=al2_o3_gam3, sigma_diag=al2_o3_sig3*mp.Vector3(1,1,0))]

al2_o3_frq1 = 1/(0.0740288*um_scale)
al2_o3_gam1 = 0
al2_o3_sig1 = 1.5039759
al2_o3_frq2 = 1/(0.1216529*um_scale)
al2_o3_gam2 = 0
al2_o3_sig2 = 0.55069141
al2_o3_frq3 = 1/(20.072248*um_scale)
al2_o3_gam3 = 0
al2_o3_sig3 = 6.5927379

al2_o3_susc_e = [mp.LorentzianSusceptibility(frequency=al2_o3_frq1, gamma=al2_o3_gam1, sigma_diag=al2_o3_sig1*mp.Vector3(0,0,1)),
                mp.LorentzianSusceptibility(frequency=al2_o3_frq2, gamma=al2_o3_gam2, sigma_diag=al2_o3_sig2*mp.Vector3(0,0,1)),
                mp.LorentzianSusceptibility(frequency=al2_o3_frq3, gamma=al2_o3_gam3, sigma_diag=al2_o3_sig3*mp.Vector3(0,0,1))]

al2_o3_aniso = mp.Medium(epsilon=1, E_susceptibilities=al2_o3_susc_o+al2_o3_susc_e, valid_freq_range=al2_o3_range)

#------------------------------------------------------------------
# yttrium oxide (Y2O3) from Y. Nigara, Japanese J. of Applied Physics, Vol. 7, pp. 404-8, 1968
# ref: https://refractiveindex.info/?shelf=main&book=Y2O3&page=Nigara
# wavelength range: 0.25 - 9.6 um

y2_o3_range = mp.FreqRange(min=um_scale/9.6, max=um_scale/0.25)

y2_o3_frq1 = 1/(0.1387*um_scale)
y2_o3_gam1 = 0
y2_o3_sig1 = 2.578
y2_o3_frq2 = 1/(22.936*um_scale)
y2_o3_gam2 = 0
y2_o3_sig2 = 3.935

y2_o3_susc = [mp.LorentzianSusceptibility(frequency=y2_o3_frq1, gamma=y2_o3_gam1, sigma=y2_o3_sig1),
             mp.LorentzianSusceptibility(frequency=y2_o3_frq2, gamma=y2_o3_gam2, sigma=y2_o3_sig2)]

y2_o3 = mp.Medium(epsilon=1.0, E_susceptibilities=y2_o3_susc, valid_freq_range=y2_o3_range)

#------------------------------------------------------------------
# undoped yttrium aluminum garnet (YAG) from D.E. Zelmon et al., Applied Optics, Vol. 37, 4933-5, 1998
# ref: https://refractiveindex.info/?shelf=main&book=Y3Al5O12&page=Zelmon
# wavelength range: 0.4 - 5.0 um

yag_range = mp.FreqRange(min=um_scale/5.0, max=um_scale/0.4)

yag_frq1 = 1/(0.1088577052853862*um_scale)
yag_gam1 = 0
yag_sig1 = 2.28200
yag_frq2 = 1/(16.814695953242804*um_scale)
yag_gam2 = 0
yag_sig2 = 3.27644

yag_susc = [mp.LorentzianSusceptibility(frequency=yag_frq1, gamma=yag_gam1, sigma=yag_sig1),
            mp.LorentzianSusceptibility(frequency=yag_frq2, gamma=yag_gam2, sigma=yag_sig2)]

yag = mp.Medium(epsilon=1.0, E_susceptibilities=yag_susc, valid_freq_range=yag_range)

#------------------------------------------------------------------
# cadmium telluride (CdTe) from D.T.F. Marple, J. Applied Physics, Vol. 35, pp. 539-42, 1964
# ref: https://refractiveindex.info/?shelf=main&book=CdTe&page=Marple
# wavelength range: 0.86 - 2.5 um

cd_te_range = mp.FreqRange(min=um_scale/2.5, max=um_scale/0.86)

cd_te_frq1 = 1/(0.6049793384901669*um_scale)
cd_te_gam1 = 0
cd_te_sig1 = 1.53

cd_te_susc = [mp.LorentzianSusceptibility(frequency=cd_te_frq1, gamma=cd_te_gam1, sigma=cd_te_sig1)]

cd_te = mp.Medium(epsilon=5.68, E_susceptibilities=cd_te_susc, valid_freq_range=cd_te_range)
