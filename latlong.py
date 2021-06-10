import fruitbat
import numpy as np
dat_zhang=[]
dat_inoue=[]
dat_ioka=[]

#for i in np.linspace(10, 5000, num=500):

#    frb_zhang = fruitbat.Frb(i,method="Zhang2018")
 #   frb_ioka = fruitbat.Frb(i,method="Ioka2003")
  #  frb_inoue = fruitbat.Frb(i,method="Inoue2004")

#    dat_zhang.append((i, frb_zhang.calc_redshift(method="Zhang2018"), frb_zhang.calc_comoving_distance().value, frb_zhang.calc_luminosity_distance().value ))
 
 #   dat_inoue.append((i, frb_inoue.calc_redshift(method="Inoue2004"), frb_inoue.calc_comoving_distance().value, frb_inoue.calc_luminosity_distance().value ))
 
 #  dat_ioka.append((i, frb_ioka.calc_redshift(method="Ioka2003"), frb_ioka.calc_comoving_distance().value, frb_ioka.calc_luminosity_distance().value ))

#np.savetxt('distance_zhang.dat',dat_zhang)
#np.savetxt('distance_inoue.dat',dat_inoue)
#np.savetxt('distance_ioka.dat',dat_ioka)
test=[]
for i in np.linspace(-90,90,10):
    for j in np.linspace(-90,90,10):
        gl_var=str(i)
        gb_var=str(j)
        frb_zhang = fruitbat.Frb(600,method="Zhang2018",gl=gl_var,gb=gb_var)
        test.append((i,frb_zhang.calc_dm_galaxy().value,frb_zhang.calc_redshift(method="Zhang2018")))
np.savetxt('latlon.dat',test)

