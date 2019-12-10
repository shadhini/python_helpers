import geopandas as gpd


#### read shape file ####
shp_file_data = gpd.read_file('sub_subcatchments.shp')

# data type
# print(type(shp_file_data))

# print head
# print(shp_file_data.head())

# plot data
# this needs libraries 'matplotlib', 'descartes' to be installed on the execution environment
# shp_file_data.plot()


#### CRS :: Coordinate Reference System ####

# print(shp_file_data.crs)

#### Geometries ####
# print(shp_file_data['geometry'].head())

selection = shp_file_data[0:5]

# for index, row in selection.iterrows():
#    poly_area = row['geometry'].area
#    print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

shp_file_data['area'] = None

for index, row in shp_file_data.iterrows():
    print(row['geometry'])
    # print(index)
    # print(type(row['geometry']))
    # print((row['geometry']).area)
    # shp_file_data.loc[index, 'area'] = row['geometry'].area

# print(shp_file_data['area'].head(2))

