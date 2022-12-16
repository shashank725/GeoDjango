import geopandas as gpd
import matplotlib.pyplot as plt

# Importing an ESRI Shapefile and plotting it using GeoPandas
# districts = gpd.read_file(r'D:\GeoDelta Labs\12. Introduction to GeoPandas\Shapefiles\districts.shp')
districts = gpd.read_file(r'/media/ghost/Data/Programing/Web/Django Projects/GeoDjango/GeoPandas/Shapefiles/districts.shp')
districts.plot(cmap = 'hsv', edgecolor = 'black', column = 'district')
print(districts.head())

area_of_interest = gpd.read_file(r'/media/ghost/Data/Programing/Web/Django Projects/GeoDjango/GeoPandas/Shapefiles/area_of_interest.shp')
area_of_interest.plot()
print(area_of_interest)

atms = gpd.read_file(r'/media/ghost/Data/Programing/Web/Django Projects/GeoDjango/GeoPandas/Shapefiles/atms.shp')
print(atms)

# # Plot the figures side by side 
# fig, (ax1, ax2) = plt.subplots(nrows = 2, figsize = (10,8))
# districts.plot(ax = ax1, cmap = 'hsv', edgecolor = 'black', column = 'district')
# area_of_interest.plot(ax = ax2, color = 'green')

# # Plotting multiple layers
# fig, ax = plt.subplots(figsize = (10,8))
# districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
# area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
# atms.plot(ax = ax, color = 'black', markersize = 14)

# Reprojecting GeoPandas GeoDataFrames
fig, ax = plt.subplots(figsize = (8,6))
districts = districts.to_crs(epsg = 32629)
districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
area_of_interest = area_of_interest.to_crs(epsg = 32629)
area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')

# Intersecting Layers
districts_in_aoi = gpd.overlay(districts, area_of_interest, how = 'intersection')
districts_in_aoi.plot(edgecolor = 'red')
print(districts_in_aoi)

# Calculating the areas of the intersected layer 
districts_in_aoi['area'] = districts_in_aoi.area/1000000
print(districts_in_aoi['area'])

# Exporting GeoPandas GeoDataFrames into an ESRI Shapefile
districts_in_aoi.to_file('districts_within_aoi.shp', driver = "ESRI Shapefile")



















