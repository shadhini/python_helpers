import sys
import getopt
import os, csv
import json
import traceback
from datetime import datetime, timedelta

import operator
import collections
from math import acos, cos, sin, radians

import pandas as pd
import numpy as np
import geopandas as gpd
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, Point

"""
divide points set to thiessan polygon created based on active observational rain gauges 
to decide which observation to be used for the point based in the polygon each point belongs to
"""


def read_csv(file_name):
    with open(file_name, 'r') as f:
        data = [list(line) for line in csv.reader(f)][1:]
    return data


def _voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.
    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.
    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.
    from: https://stackoverflow.com/questions/20515554/colorize-voronoi-diagram
    """
    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()
    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()
    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]
        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue
        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue
            # Compute the missing endpoint of an infinite ridge
            t = vor.points[p2] - vor.points[p1]  # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius
            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:, 1] - c[1], vs[:, 0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]
        # finish
        new_regions.append(new_region.tolist())
    return new_regions, np.asarray(new_vertices)


def get_voronoi_polygons(points_dict, shape_file, shape_attribute=None, output_shape_file=None, add_total_area=True):
    """
    :param points_dict: dict of points {'id' --> [lon, lat]}
    :param shape_file: shape file path of the area
    :param shape_attribute: attribute list of the interested region [key, value]
    :param output_shape_file: if not none, a shape file will be created with the output
    :param add_total_area: if true, total area shape will also be added to output
    :return:
    geo_dataframe with voronoi polygons with columns ['id', 'lon', 'lat','area', 'geometry'] with last row being the area of the
    shape file
    """
    if shape_attribute is None:
        shape_attribute = ['OBJECTID', 1]

    shape_df = gpd.GeoDataFrame.from_file(shape_file)
    shape_polygon_idx = shape_df.index[shape_df[shape_attribute[0]] == shape_attribute[1]][0]
    shape_polygon = shape_df['geometry'][shape_polygon_idx]

    ids = [p if type(p) == str else np.asscalar(p) for p in points_dict.keys()]
    points = np.array(list(points_dict.values()))[:, :2]
    vor = Voronoi(points)

    regions, vertices = _voronoi_finite_polygons_2d(vor)

    data = []
    for i, region in enumerate(regions):
        polygon = Polygon([tuple(x) for x in vertices[region]])
        if polygon.intersects(shape_polygon):
            intersection = polygon.intersection(shape_polygon)
            data.append({'id': ids[i], 'lon': vor.points[i][0], 'lat': vor.points[i][1], 'area': intersection.area,
                         'geometry': intersection
                         })
    df = gpd.GeoDataFrame(data, columns=['id', 'lon', 'lat', 'area', 'geometry'], crs=shape_df.crs)
    if output_shape_file is not None:
        df.to_file(output_shape_file)

    return df


def divide_flo2d_grids_to_polygons(flo2d_grids, polygons):

    for grid in flo2d_grids:
        point = Point(float(grid[1]), float(grid[2]))

        for index, row in polygons.iterrows():
            polygon = polygons.iloc[index]['geometry']
            if point.within(polygon):
                grid.append(polygons.iloc[index]['id'])
                continue

    return flo2d_grids


corrected_rf_df = pd.read_csv("/home/shadhini/dev/repos/shadhini/python_helpers/thiessen_polygon/corrected_rf.csv",
                              delimiter=',')
flo2d_grids = read_csv('/home/shadhini/dev/repos/shadhini/python_helpers/thiessen_polygon/flo2d_250m.csv')
# [Grid_ ID, X(longitude), Y(latitude)]


distinct_stations = corrected_rf_df.groupby(['longitude', 'latitude']).size()

points_dict = {}
count = 1000
for index, row in distinct_stations.iteritems():
    points_dict['point_{}'.format(count)] = [index[0], index[1]]
    count += 1

polygons = get_voronoi_polygons(points_dict=points_dict,
                                shape_file="/home/shadhini/dev/repos/shadhini/python_helpers/thiessen_polygon/250m_model/250m_model.shp",
                                shape_attribute=['Id', 0],
                                output_shape_file="/home/shadhini/dev/repos/shadhini/python_helpers/thiessen_polygon/250m_model/output/output.shp",
                                add_total_area=True)

flo2d_grid_polygon_map = divide_flo2d_grids_to_polygons(flo2d_grids=flo2d_grids, polygons=polygons)

print(flo2d_grid_polygon_map)