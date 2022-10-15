import netCDF4
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd

nc = netCDF4.Dataset("sample_data_2.nc", "r", format="NETCDF4")

print(nc.variables.keys())

lat = nc.variables["lat"][:]
lon = nc.variables["lon"][:]

time_var = nc.variables["time"]
dtime = netCDF4.num2date(time_var[:], time_var.units)

sst = nc.variables["sea_surface_temperature"]

# print(sst)

# print(lat)
# print(lon)
# print(dtime[0])

print(lat[0])
print(lat[4320 - 1])

print(lon[0])
print(lon[8640 - 1])


# print(sst[0, 2000, 2000])

# # loop from 0 to 4320
# for i in range(2000, 4320):
#     for j in range(2000, 8640):
#         print(lat[i], lon[j], sst[0, i, j])


def getLatIndex(lat):
    max_index = 4320
    min_index = 0
    max_lat = -90
    min_lat = 90

    factor = max_index / (max_lat - min_lat)

    return int((max_index / 2) + factor * lat)


def getLonIndex(lon):
    max_index = 8640
    min_index = 0
    max_lon = 180
    min_lon = -180

    factor = max_index / (max_lon - min_lon)

    return int((max_index / 2) + factor * lon)


print(getLonIndex(85))
print(lon[getLonIndex(85)])
