import os
import numpy as np
from netCDF4 import Dataset
from datetime import datetime, timedelta

from logger import logger


def get_two_element_average(prcp, return_diff=True):
    avg_prcp = (prcp[1:] + prcp[:-1]) * 0.5
    if return_diff:
        return avg_prcp - np.insert(avg_prcp[:-1], 0, [0], axis=0)
    else:
        return avg_prcp


def get_per_time_slot_values(prcp):
    per_interval_prcp = (prcp[1:] - prcp[:-1])
    return per_interval_prcp


def datetime_utc_to_lk(timestamp_utc, shift_mins=0):
    return timestamp_utc + timedelta(hours=5, minutes=30 + shift_mins)


# def view_netcdf_data(rainc_net_cdf_file_path, rainnc_net_cdf_file_path):
#     """
#
#         :param pool: database connection pool
#         :param rainc_net_cdf_file_path:
#         :param rainnc_net_cdf_file_path:
#         :param source_id:
#         :param variable_id:
#         :param unit_id:
#         :param tms_meta:
#         :return:
#
#         rainc_unit_info:  mm
#         lat_unit_info:  degree_north
#         time_unit_info:  minutes since 2019-04-02T18:00:00
#         """
#
#     if not os.path.exists(rainc_net_cdf_file_path):
#         # logger.warning('no rainc netcdf')
#         print('no rainc netcdf')
#     elif not os.path.exists(rainnc_net_cdf_file_path):
#         # logger.warning('no rainnc netcdf')
#         print('no rainnc netcdf')
#     else:
#
#         """
#         RAINC netcdf data extraction
#         """
#         nc_fid = Dataset(rainc_net_cdf_file_path, mode='r')
#
#         time_unit_info = nc_fid.variables['Times'].units
#
#         time_unit_info_list = time_unit_info.split(' ')
#
#         lats = nc_fid.variables['XLAT'][0, :, 0]
#         lons = nc_fid.variables['XLONG'][0, 0, :]
#
#         lon_min = lons[0].item()
#         lat_min = lats[0].item()
#         lon_max = lons[-1].item()
#         lat_max = lats[-1].item()
#         print('[lon_min, lat_min, lon_max, lat_max] :', [lon_min, lat_min, lon_max, lat_max])
#
#         lat_inds = np.where((lats >= lat_min) & (lats <= lat_max))
#         lon_inds = np.where((lons >= lon_min) & (lons <= lon_max))
#
#         rainc = nc_fid.variables['RAINC'][:, lat_inds[0], lon_inds[0]]
#
#         """
#         RAINNC netcdf data extraction
#         """
#         nnc_fid = Dataset(rainnc_net_cdf_file_path, mode='r')
#
#         rainnc = nnc_fid.variables['RAINNC'][:, lat_inds[0], lon_inds[0]]
#
#         # times = list(set(nc_fid.variables['XTIME'][:]))  # set is used to remove duplicates
#         times = nc_fid.variables['Times'][:]
#         print(sorted(set(times))[-2])
#
#         prcp = rainc + rainnc
#
#         nc_fid.close()
#         nnc_fid.close()
#
#         diff = get_per_time_slot_values(prcp)
#         print('diff : ', len(diff))
#
#         width = len(lons)
#         height = len(lats)
#
#         for y in range(1):#height # lat
#             for x in range(1): # lon
#
#                 lat = float(lats[y])
#                 lon = float(lons[x])
#
#                 data_list = []
#                 # generate timeseries for each station
#                 for i in range(len(prcp)):
#                     ts_time = datetime.strptime(time_unit_info_list[2], '%Y-%m-%dT%H:%M:%S') + timedelta(
#                             minutes=times[i].item())
#                     t = datetime_utc_to_lk(ts_time, shift_mins=0)
#                     data_list.append([t.strftime('%Y-%m-%d %H:%M:%S'), float(prcp[i, y, x])])
#                     # print (float(diff[i, 146, 19]))
#                     # print([t.strftime('%Y-%m-%d %H:%M:%S'), float(prcp[i, y, x])])
#                     # print("original" ,[t.strftime('%Y-%m-%d %H:%M:%S'), float(prcp[i, y, x])])
#                     # if i == 0:
#                     #    print([t.strftime('%Y-%m-%d %H:%M:%S'), float(prcp[i, y, x])])
#                     # else:
#                     #     print ([t.strftime('%Y-%m-%d %H:%M:%S'), float(diff[i-1, y, x])])
#                 print(data_list)


def view_netcdf_data_Jean(rainnc_net_cdf_file_path):
    """
        :param pool: database connection pool
        :param rainc_net_cdf_file_path:
        :param rainnc_net_cdf_file_path:
        :param source_id:
        :param variable_id:
        :param unit_id:
        :param tms_meta:
        :return:
        rainc_unit_info:  mm
        lat_unit_info:  degree_north
        time_unit_info:  minutes since 2019-04-02T18:00:00
        """

    if not os.path.exists(rainnc_net_cdf_file_path):
        logger.warning('no rainnc netcdf')
        print('no rainnc netcdf')
    else:

        """
        RAINNC netcdf data extraction
        """
        nnc_fid = Dataset(rainnc_net_cdf_file_path, mode='r')

        time_unit_info = nnc_fid.variables['Times'].units

        time_unit_info_list = time_unit_info.split(' ')

        lats = nnc_fid.variables['XLAT'][0, :, 0]
        lons = nnc_fid.variables['XLONG'][0, 0, :]

        lon_min = lons[0].item()
        lat_min = lats[0].item()
        lon_max = lons[-1].item()
        lat_max = lats[-1].item()
        print('[lon_min, lat_min, lon_max, lat_max] :', [lon_min, lat_min, lon_max, lat_max])

        lat_inds = np.where((lats >= lat_min) & (lats <= lat_max))
        lon_inds = np.where((lons >= lon_min) & (lons <= lon_max))

        rainnc = nnc_fid.variables['RAINNC'][:, lat_inds[0], lon_inds[0]]

        times = nnc_fid.variables['Times'][:]

        nnc_fid.close()

        width = len(lons)
        height = len(lats)

        count = 1
        for y in range(height):#height # lat
            for x in range(width): # lon

                count += 1
                lat = float(lats[y])
                lon = float(lons[x])
                print(count, lat, lon)

                data_list = []
                # generate timeseries for each station
                for i in range(len(rainnc)):
                    ts_time = datetime.strptime(time_unit_info_list[2], '%Y-%m-%dT%H:%M:%S') + timedelta(
                            minutes=times[i].item())
                    t = datetime_utc_to_lk(ts_time, shift_mins=0)
                    data_list.append([t.strftime('%Y-%m-%d %H:%M:%S'), float(rainnc[i, y, x])])
                    print([t.strftime('%Y-%m-%d %H:%M:%S'), float(rainnc[i, y, x])])


def view_netcdf_data(net_cdf_file_path):
    """


        rainc_unit_info:  mm
        lat_unit_info:  degree_north
        time_unit_info:  minutes since 2019-04-02T18:00:00
        """

    if not os.path.exists(net_cdf_file_path):
        # logger.warning('no netcdf :: {}'.format(net_cdf_file_path))
        print('no netcdf :: {}'.format(net_cdf_file_path))
    else:

        """
        RAINNC netcdf data extraction
        """
        nnc_fid = Dataset(net_cdf_file_path, mode='r')

        # time_unit_info = nnc_fid.variables['Times'].units

        # time_unit_info_list = time_unit_info.split(' ')

        lats = nnc_fid.variables['XLAT'][0, :, 0]
        lons = nnc_fid.variables['XLONG'][0, 0, :]

        lon_min = lons[0].item()
        lat_min = lats[0].item()
        lon_max = lons[-1].item()
        lat_max = lats[-1].item()
        print('[lon_min, lat_min, lon_max, lat_max] :', [lon_min, lat_min, lon_max, lat_max])

        lat_inds = np.where((lats >= lat_min) & (lats <= lat_max))
        lon_inds = np.where((lons >= lon_min) & (lons <= lon_max))

        rainnc = nnc_fid.variables['RAINNC'][:, lat_inds[0], lon_inds[0]]

        times = np.array([''.join([y.decode() for y in x]) for x in nnc_fid.variables['Times'][:]])
        # times = nnc_fid.variables['Times'][:, lat_inds[0], lon_inds[0]]

        nnc_fid.close()

        width = len(lons)
        height = len(lats)

        count = 1
        for y in range(height):#height # lat
            for x in range(width): # lon

                count += 1
                lat = float(lats[y])
                lon = float(lons[x])
                print("###########", count, lat, lon, "###########")

                data_list = []
                # generate timeseries for each station
                for i in range(len(rainnc)):
                    # ts_time = datetime.strptime(time_unit_info_list[2], '%Y-%m-%dT%H:%M:%S') + timedelta(
                    #         minutes=times[i].item())
                    # t = datetime_utc_to_lk(ts_time, shift_mins=0)
                    t = datetime_utc_to_lk(datetime.strptime(times[i], '%Y-%m-%d_%H:%M:%S'), shift_mins=0)
                    # data_list.append([t.strftime('%Y-%m-%d %H:%M:%S'), float(rainnc[i, y, x])])
                    print([t.strftime('%Y-%m-%d %H:%M:%S'), float(rainnc[i, y, x])])


# rainc_id = Dataset("wrfout_d03_2019-08-03_00:00:00", mode='r')
# # rainnc_id = Dataset("/home/shadhini/dev/repos/shadhini/curw_helpers/netcdf_utils/wrfv4/RAINNC_2019-04-18_A.nc", mode='r')
#
# print(rainc_id.variables.keys())
# print(rainc_id.variables['Times'])
# print(rainc_id.variables['RAINC'])
# print (rainc_id.variables['RAINC'][:,46,24])
# print (rainnc_id.variables['RAINNC'][:,146,19])

# view_netcdf_data("/home/shadhini/dev/repos/shadhini/curw_helpers/netcdf_utils/RAINC_2019-05-03_A.nc",
#         "/home/shadhini/dev/repos/shadhini/curw_helpers/netcdf_utils/RAINNC_2019-05-03_A.nc")

view_netcdf_data("wrfout_d03_2019-08-03_00:00:00")