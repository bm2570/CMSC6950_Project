import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import sys

fname=sys.argv[1] #use latlon data files
plottype=sys.argv[2] # use DM for dispersion measure and Z for redshift
if fname=='latlon_zhang.dat':
    title='Zhang2018'
if fname=='latlon_ioka.dat':
    title='Ioka2003'
if fname=='latlon_inoue.dat':
    title='Inoue2004'
    
# Load in data
dat = np.genfromtxt(fname, delimiter=' ',skip_header=0)
lat = dat[:,0] #Latitude
lon = dat[:,1] #Longitude

# Converting to np arrays
X, Y, Z, = np.array([]), np.array([]), np.array([])
for i in range(len(lat)):
        X = np.append(X,lat[i])
        Y = np.append(Y,lon[i])

# Creating x-y points to define the space (associated with z-coordinate)
xi = np.linspace(X.min(),X.max(),300)
yi = np.linspace(Y.min(),Y.max(),300)

if plottype=='DM': ## DM contribution
    Z_dat = dat[:,2] 
    Z = np.array([])
    for i in range(len(lat)):
        Z = np.append(Z,Z_dat[i])

# Need to make a 2d array for z axis
    zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]))

# Creating heat map
    fig1=plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow)
    cbar1=plt.colorbar()  
    cbar1.set_label('DM [pc cm$^{-3}$]')
    plt.suptitle(title)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.savefig('DM_heatplot_'+title+'.png')
    plt.show()

if plottype=='Z': ## Redshift
    
    Z_dat = dat[:,3] 
    Z = np.array([])
    for i in range(len(lat)):
        Z = np.append(Z,Z_dat[i])
# Need to make a 2d array for z axis
    zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]))
        
# Creating heat map
    fig2=plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow)#,vmax=zmax, vmin=zmin)
    cbar2=plt.colorbar()  
    cbar2.set_label('Redshift')
    plt.suptitle(title)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.savefig('redshift_heatplot_'+title+'.png')
    plt.show()

