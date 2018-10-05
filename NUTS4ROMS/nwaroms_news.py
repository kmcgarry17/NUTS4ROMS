import lib_Global_NEWS_to_ROMS as lgn
import xarray as xr

# pick a ROMS domain
grdfile='/Users/raphael/STORAGE/ROMS/GRIDS/NWA_grd.nc'
csvdir = './data/'

nwanews = lgn.news2roms(grdfile)
nwanews.read_database(csvdir)
nwanews.extract_domain()

# do this if you want to see locations or rivers mouth
#nwanews.plot_river_mouth(db='domain')

nwanews.move_rivermouth2roms()

# you can pass a list of rivers to check, will show spreading performed
#no3_conc = nwanews.create_rivers_input('NO3_CONC',river_checklist=['Susquehanna'])
no3_conc = nwanews.create_rivers_input('NO3_CONC',plot_result=False)
po4_conc = nwanews.create_rivers_input('PO4_CONC',plot_result=False)
# you can do the same for all other nutrients

# create the output file with xarray
grd = xr.open_dataset(grdfile)
ds = xr.Dataset({'no3_conc': (['eta_rho','xi_rho'], no3_conc),
                 'po4_conc': (['eta_rho','xi_rho'], po4_conc),
                # add other nutrient to dataset
                },
                coords={'lon_rho': (['eta_rho', 'xi_rho'], grd.lon_rho),
                        'lat_rho': (['eta_rho', 'xi_rho'], grd.lat_rho)} )
ds.to_netcdf('nutrients_conc_NWA.nc')
