import matplotlib.pyplot as plt
import numpy as np

#Importing data 
zhang = np.genfromtxt('latcut_zhang.dat', delimiter=' ',skip_header=0)
lat= zhang[:,0]
lon_zhang = zhang[:,1]
calcdm_zhang = zhang[:,2]
redshift_zhang = zhang[:,3]

ioka = np.genfromtxt('latcut_ioka.dat', delimiter=' ',skip_header=0)
lon_ioka = ioka[:,1]
calcdm_ioka = ioka[:,2]
redshift_ioka = ioka[:,3]

inoue = np.genfromtxt('latcut_inoue.dat', delimiter=' ',skip_header=0)
lon_inoue = inoue[:,1]
calcdm_inoue = inoue[:,2]
redshift_inoue = inoue[:,3]

plt.figure(1)
plt.subplot(111)
plt.plot( lon_zhang,calcdm_zhang,'k--',color='green')
plt.subplot(111)
plt.plot( lon_ioka,calcdm_ioka,'kv', color='red')
plt.subplot(111)
plt.plot( lon_inoue,calcdm_inoue,'k.', color='blue')
plt.ylabel('DM [pc cm$^{-3}$]')
plt.xlabel('Longitude [$^\circ$]')
plt.suptitle('Dispersion Measure (DM) vs Longitude With Latitude=$-0.909^\circ$')
plt.legend(["Zhang2018", "Ioka2003", "Inoue2004"])
plt.savefig('DM_vs_longitude.png',dpi=1000)

plt.figure(2)
plt.subplot(111)
plt.plot( lon_zhang,redshift_zhang)
plt.subplot(111)
plt.plot( lon_ioka,redshift_ioka)
plt.subplot(111)
plt.plot( lon_inoue,redshift_inoue)
plt.ylabel('Z')
plt.xlabel('Longitude [$^\circ$]')
plt.suptitle('Redshift (Z) vs Longitude With Latitude=$-0.909^\circ$')
plt.legend(["Zhang2018", "Ioka2003", "Inoue2004"])
plt.savefig('Z_vs_longitude.png',dpi=1000)
