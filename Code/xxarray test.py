import cartopy
import numpy as np
import pandas as pd
import xarray as xr
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf


# Loads netcdf file into memory
ds_disk = xr.open_dataset("C:/Users/chens/Documents/Hurricanes/Data/HURSAT-avhrr_v05_2005236N23285_KATRINA/2005/2005236N23285.KATRINA.2005.08.29.0824.20.NOAA-18.110.hursat-avhrr.v05.nc")

# Initiliaze variables
lon = ds_disk.lon
lat = ds_disk.lat
ch1_ref = ds_disk.CH1_REF
ch2_ref = ds_disk.CH2_REF
ch3_temp = ds_disk.CH3_TEMP
cent_lat = ds_disk.CentLat
cent_lon = ds_disk.CentLon
pres = ds_disk.pres_for_mapping

print(ds_disk.time_wmo)
# print(ch2_ref)
# This actually plots the data
fig = plt.figure()
ax = fig.add_subplot(projection=ccrs.PlateCarree())
ds_disk.CH1_REF.plot(ax=ax)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.STATES)
# plt.title(ds_disk.time_wmo[0])


plt.show()
