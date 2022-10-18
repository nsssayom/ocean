import netCDF4
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# read the netcdf file
nc = netCDF4.Dataset("sample_data_4.nc", "r", format="NETCDF4")

# get all lat and lon values
lat = nc.variables["lat"][:]
lon = nc.variables["lon"][:]


# lat starts at -90 and ends at 90
# lat has 17999 indexes
# this function will return the index of the closest value to the given value
def get_lat_index(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


# lon starts at -180 and ends at 180
# lon has 36000 indexes
# this function will return the index of the closest value to the given value
def get_lon_index(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


lats = lat[get_lat_index(lat, 15) : get_lat_index(lat, 25)]
lons = lon[get_lon_index(lon, 85) : get_lon_index(lon, 95)]


sst = nc.variables["analysed_sst"][
    0,
    get_lat_index(lat, 15) : get_lat_index(lat, 25),
    get_lon_index(lon, 85) : get_lon_index(lon, 95),
]

# take every 10th value from the sst array
sst = sst[::10, ::10]

# create a basemap instance
map = Basemap(
    projection="merc",
    llcrnrlon=85.0,
    llcrnrlat=15.0,
    urcrnrlon=95.0,
    urcrnrlat=25.0,
    resolution="i",
)
map.drawcoastlines()
map.drawcountries()
map.drawlsmask(land_color="#A1887F", ocean_color="#4FC3F7")

lons, lats = np.meshgrid(lon, lat)
x, y = map(lons, lats)

map.pcolormesh(x, y, sst, cmap=plt.cm.magma_r)

# add colorbar and title besides the plot
plt.colorbar(orientation="vertical")
plt.title("Sea Surface Temperature")

plt.show()
