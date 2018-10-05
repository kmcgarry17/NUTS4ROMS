import lib_Global_NEWS_to_ROMS as lgn
import pyroms
import xarray as xr

# pick a ROMS domain
grdname='NWA'
csvdir = './data/'

nwanews = lgn.news2roms(grdname)
nwanews.read_database(csvdir)
nwanews.extract_domain()

# do this if you want to see locations or rivers mouth
#nwanews.plot_river_mouth(db='domain')

nwanews.move_rivermouth2roms()

# you can pass a list of rivers to check, will show spreading performed
#no3_conc = nwanews.create_rivers_input('NO3_CONC',river_checklist=['Susquehanna'])
no3_conc = nwanews.create_rivers_input('NO3_CONC',plot_result=False)

# create the output file with xarray
grd = pyroms.grid.get_ROMS_grid(grdname)
ds = xr.Dataset({'no3_conc': (['eta_rho','xi_rho'], no3_conc)},
                coords={'lon_rho': (['eta_rho', 'xi_rho'], grd.hgrid.lon_rho),
                        'lat_rho': (['eta_rho', 'xi_rho'], grd.hgrid.lat_rho)} )
ds.to_netcdf('no3_conc_NWA.nc')
