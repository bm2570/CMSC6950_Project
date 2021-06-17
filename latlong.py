### This script calculates the dispersion measure and redshift over the range of latitude and longitude coordinates from [-90,90] degrees for the "Zhang2018", "Ioka2003", and "Inoue2004" methods
import fruitbat
import numpy as np
import sys

fname=sys.argv[1]
dat=[]

for i in np.linspace(-90,90,100):
    for j in np.linspace(-90,90,100):
        gl_var=str(i)
        gb_var=str(j)
        frb_dat = fruitbat.Frb(600,method=fname,gl=gl_var,gb=gb_var)
        dat.append((i,j,frb_dat.calc_dm_galaxy().value,frb_dat.calc_redshift(method=fname)))

np.savetxt('latlon_'+fname+'.dat',dat)

