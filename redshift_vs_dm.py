import fruitbat
import numpy as np
##This script calculates the redshift as a function of dispersion measure (dm), which we iterate from 0 to 5000.
dat=[]
for i in np.linspace(0, 5000, num=1000):
    #frb= fruitbat.Frb(i, gl="7.8", gb="-51.9", name="FRB180110")
    frb = fruitbat.Frb(i)
    #test_calc=frb.calc_dm_galaxy()
    dat.append((i, frb.calc_redshift(method="Zhang2018"),frb.calc_redshift(method="Ioka2003"),frb.calc_redshift(method="Inoue2004") ))
np.savetxt('data.dat',dat)
