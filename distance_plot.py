import matplotlib.pyplot as plt
import numpy as np

#Importing data 
zhang = np.genfromtxt('distance_Zhang2018.dat', delimiter=' ',skip_header=0)
dm = zhang[:,0]
zhang_redshift = zhang[:,1]
zhang_comoving = zhang[:,2]
zhang_lum = zhang[:,3]

inoue = np.genfromtxt('distance_Inoue2004.dat', delimiter=' ',skip_header=0)
inoue_redshift = inoue[:,1]
inoue_comoving = inoue[:,2]
inoue_lum = inoue[:,3]

ioka = np.genfromtxt('distance_Ioka2003.dat', delimiter=' ',skip_header=0)
ioka_redshift = ioka[:,1]
ioka_comoving = ioka[:,2]
ioka_lum = ioka[:,3]


#Z(DM) plot
plt.figure(1)
plt.subplot(111)
plt.plot( dm,zhang_redshift)
plt.subplot(111)
plt.plot(dm,ioka_redshift)
plt.subplot(111)
plt.plot(dm,inoue_redshift)
plt.xlabel('DM [pc cm$^{-3}$]')
plt.xticks(np.arange(0, 5001, step=500))
plt.ylabel('Z')
plt.suptitle('Redshift (Z) vs Dispersion Measure (DM)')
plt.legend(["Zhang2018", "Ioka2003", "Inoue2004"])
plt.savefig('Z_vs_DM.png',dpi=1000)

#d_C(DM) and d_L(DM) plots
plt.figure(2)
ax1=plt.subplot(211)
ax1.title.set_text('Comoving Distance (d$_C$) vs Dispersion Measure (DM)')
ax1.axes.xaxis.set_ticks([])
plt.plot( dm,zhang_comoving)
plt.subplot(211)
plt.plot(dm,ioka_comoving)
plt.subplot(211)
plt.plot(dm,inoue_comoving)
plt.legend(["Zhang2018", "Ioka2003", "Inoue2004"])
plt.ylabel('d$_C$ [Mpc]')
ax2=plt.subplot(212)
ax2.title.set_text('Luminosity Distance (d$_L$) vs Dispersion Measure (DM)')
plt.plot( dm,zhang_lum)
plt.subplot(212)
plt.plot(dm,ioka_lum)
plt.subplot(212)
plt.plot(dm,inoue_lum)
plt.legend(["Zhang2018", "Ioka2003", "Inoue2004"])
plt.ylabel('d$_L$ [Mpc]')
plt.xlabel('DM [pc cm$^{-3}$]')
plt.savefig('distance_vs_DM.png',dpi=1000)
