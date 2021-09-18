import netCDF4 as nc
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# Use basemap with center lon and lat for the center of map
dp = nc.Dataset("C:/Users/chens/Documents/Hurricanes/Data/HURSAT-avhrr_v05_2005236N23285_KATRINA/2005/2005236N23285.KATRINA.2005.08.25.1842.25.NOAA-18.053.hursat-avhrr.v05.nc", "r", format="NETCDF4")

lat = dp['lat'][:]
lon = dp['lon'][:]

#lons, lats = np.meshgrid(lon, lat)
x = []
y = []
pressure = []
for g in lon:
    x.append(g)
for j in lat:
    y.append(j)
#print(x)
#print(y)

cent_lat = dp['CentLat'][0]
cent_lon = dp['CentLon'][0]
ch3_temp = dp["CH3_TEMP"][:]
pres = dp["pres_for_mapping"][:]
ch2_ref = dp["CH2_REF"][:]
print(ch2_ref)
for k in pres:
    pressure.append(k)
fig = plt.figure(figsize=(10, 10))
m = Basemap(projection='lcc', resolution='c', width=8E6, height=8E6,  lat_0=cent_lat, lon_0=cent_lon)
m.drawcoastlines()
m.drawstates()
m.drawcountries()

m.contour(x, y, pressure)
print(ch2_ref)
print(pres)

#plt.show()

# print(dp.variables)
# print(dp['CH1_REF'])


