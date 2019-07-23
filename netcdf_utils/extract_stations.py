import os
import numpy as np
from netCDF4 import Dataset

from logger import logger
from csv_utils import create_csv


def extract_stations_to_csv(net_cdf_file_path):

    if not os.path.exists(net_cdf_file_path):
        logger.warning('no netcdf')
        print('no netcdf')
    else:

        """
        netcdf station extraction
        """
        fid = Dataset(net_cdf_file_path, mode='r')

        lats = fid.variables['XLAT'][0, :, 0]
        lons = fid.variables['XLONG'][0, 0, :]

        lon_min = lons[0].item()
        lat_min = lats[0].item()
        lon_max = lons[-1].item()
        lat_max = lats[-1].item()
        print('[lon_min, lat_min, lon_max, lat_max] :', [lon_min, lat_min, lon_max, lat_max])

        lat_inds = np.where((lats >= lat_min) & (lats <= lat_max))
        lon_inds = np.where((lons >= lon_min) & (lons <= lon_max))

        fid.close()

        width = len(lons)
        height = len(lats)

        stations = [['latitude', 'longitude']]

        for y in range(height):#height
            for x in range(width):

                lat = float(lats[y])
                lon = float(lons[x])

                stations.append([lat, lon])

        create_csv('d03__A.csv', stations)


extract_stations_to_csv("/home/shadhini/Downloads/wrfv3_new_nc/d03__A.nc")

