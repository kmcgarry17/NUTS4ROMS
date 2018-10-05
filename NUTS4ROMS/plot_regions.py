import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pyroms
import numpy as np
import netCDF4 as nc
import matplotlib.cm as cm
import matplotlib.colors as cl

import cartopy.io.shapereader as shpreader
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader


def readnc(filein,varin):
        ''' read data from netcdf file '''
        fid = nc.Dataset(filein,'r')
        out = fid.variables[varin][:].squeeze()
        fid.close()
        return out

def setup_map(grdname='NWA'):
        ''' set the map, with etopo optionally '''

        datadir='./'
	grd = pyroms.grid.get_ROMS_grid(grdname)
	lonmin = grd.hgrid.lon_rho.min()
	lonmax = grd.hgrid.lon_rho.max()
	latmin = grd.hgrid.lat_rho.min()
	latmax = grd.hgrid.lat_rho.max()

        plt.figure(figsize=[8.,8.])
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent([lonmin, lonmax, latmin, latmax])
        ax.coastlines()

        return ax

ax = setup_map()

reader = shpreader.Reader('./data/NEWS2basins.shp')
basins = reader.records()
basin = next(basins)

shape_feature = ShapelyFeature(Reader('./data/NEWS2basins.shp').geometries(),
                                ccrs.PlateCarree(), edgecolor='black')
ax.add_feature(shape_feature,facecolor='blue')

#print basin
plt.show()
