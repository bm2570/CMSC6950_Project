### This script calculates the redshift, comoving distance, and luminosity distance the "Zhang2018", "Ioka2003", and "Inoue2004" methods, which each input different cosmological parameters into the integrand F(z)
import fruitbat
import numpy as np
dat_zhang=[]
dat_inoue=[]
dat_ioka=[]

### Using linspace to choose different dispersion measure (dm) values:
for i in np.linspace(10, 5000, num=500):

### Initializing fruitbat package for each of method
    frb_zhang = fruitbat.Frb(i,method="Zhang2018")
    frb_ioka = fruitbat.Frb(i,method="Ioka2003")
    frb_inoue = fruitbat.Frb(i,method="Inoue2004")

### Appending
    dat_zhang.append((i, frb_zhang.calc_redshift(method="Zhang2018"), frb_zhang.calc_comoving_distance().value, frb_zhang.calc_luminosity_distance().value ))
    dat_inoue.append((i, frb_inoue.calc_redshift(method="Inoue2004"), frb_inoue.calc_comoving_distance().value, frb_inoue.calc_luminosity_distance().value ))
    dat_ioka.append((i, frb_ioka.calc_redshift(method="Ioka2003"), frb_ioka.calc_comoving_distance().value, frb_ioka.calc_luminosity_distance().value ))

### Saving data to .dat files for later analysis
np.savetxt('distance_zhang.dat',dat_zhang)
np.savetxt('distance_inoue.dat',dat_inoue)
np.savetxt('distance_ioka.dat',dat_ioka)
