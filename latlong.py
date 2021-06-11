import fruitbat
import numpy as np


zhangdat=[]
inouedat=[]
iokadat=[]

for i in np.linspace(-90,90,180):
    for j in np.linspace(-90,90,180):
        gl_var=str(i)
        gb_var=str(j)
        frb_zhang = fruitbat.Frb(600,method="Zhang2018",gl=gl_var,gb=gb_var)
        frb_inoue = fruitbat.Frb(600,method="Inoue2004",gl=gl_var,gb=gb_var)
        frb_ioka = fruitbat.Frb(600,method="Ioka2003",gl=gl_var,gb=gb_var)
        zhangdat.append((i,j,frb_zhang.calc_dm_galaxy().value,frb_zhang.calc_redshift(method="Zhang2018")))
        iokadat.append((i,j,frb_ioka.calc_dm_galaxy().value,frb_ioka.calc_redshift(method="Ioka2003")))
        inouedat.append((i,j,frb_inoue.calc_dm_galaxy().value,frb_inoue.calc_redshift(method="Inoue2004")))

np.savetxt('latlon_zhang.dat',zhangdat)
np.savetxt('latlon_inoue.dat',inouedat)
np.savetxt('latlon_ioka.dat',iokadat)

