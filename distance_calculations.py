### This script calculates the redshift, comoving distance, and luminosity distance the "Zhang2018", "Ioka2003", and "Inoue2004" methods, which each input different cosmological parameters into the integrand F(z)
import fruitbat
import numpy as np
import sys

fname=sys.argv[1]
dat=[]
### Using linspace to choose different dispersion measure (dm) values:
for i in np.linspace(10, 5000, num=500):

### Initializing fruitbat package for each of method
    frb_dat = fruitbat.Frb(i,method=fname)
### Appending
    dat.append((i, frb_dat.calc_redshift(method=fname), frb_dat.calc_comoving_distance().value, frb_dat.calc_luminosity_distance().value ))

### Saving data to .dat files for later analysis
np.savetxt('distance_'+fname+'.dat',dat)
