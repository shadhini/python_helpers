from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
import csv
from shapely.geometry import Point, Polygon


d03_grids = pd.read_csv('d03_grids_sorted.csv', delimiter=",")
klb = gpd.read_file('klb-wgs84.shp')

# polygon = klb.iloc[0]['geometry']



#
# # print(klb['geometry'].area)
#
# print(datetime.now())
#
# for index, row in d03_grids.iterrows():
#     print(index)
#     p = Point( row['longitude'], row['latitude'])
#     if p.within(polygon):
#         d03_grids.loc[index, 'is_in'] = True
#         print("yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay")
#     else:
#         d03_grids.loc[index, 'is_in'] = False
#
# print(d03_grids)
# selected_region = d03_grids[d03_grids.is_in == True]
# print(selected_region)
# print(datetime.now())


def select_d03_grids_within_region(d03_grids, region):
    """
    param: d03_grids: pandas dataframe with 'latitude' and 'longitude' as columns
    param: region: data of a shape file containing single region (single polygon in 'geometry' field)

    returns: grids inside the polygon as a pandas dataframe with 'latitude' and 'longitude' as columns
    """

    polygon = region.iloc[0]['geometry']

    for index, row in d03_grids.iterrows():
        p = Point(row['longitude'], row['latitude'])
        if p.within(polygon):
            d03_grids.loc[index, 'is_in'] = True
        else:
            d03_grids.loc[index, 'is_in'] = False

    selected_region = d03_grids[d03_grids.is_in == True]
    return selected_region

print(select_d03_grids_within_region(d03_grids=d03_grids, region=klb))