import geopandas as gpd
shapefile = gpd.read_file("sub_subcatchments.shp")
print(shapefile)
print(shapefile.crs)
