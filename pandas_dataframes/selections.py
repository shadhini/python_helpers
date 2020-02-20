import pandas as pd


# for colum based selections
def select_sub_region(all_grids_csv_file_path, x_min, x_max, y_min, y_max):
    """
    Select sub region based on lat lon
    :param all_grids_csv_file_path: path to csv file containing longitude, latitude set
    with csv header ['longitude', 'latitude']
    :param x_min: minimum longitude of sub region
    :param x_max: maximum longitude of sub region
    :param y_min: minimum latitude of sub region
    :param y_max: maximum latitude of sub region
    :return: dataframe containing selected sub region
    """
    all_grids = pd.read_csv('d03_grids_sorted.csv', delimiter=",")

    selected_grids = all_grids[(all_grids.longitude >= x_min) & (all_grids.longitude <= x_max) &
                               (all_grids.latitude >= y_min) & (all_grids.latitude <= y_max)]

    return selected_grids


# for both column based and multi index based selections
def select_rectagular_sub_region(all_grids, lon_min=79.6, lon_max=81.0, lat_min=6.6, lat_max=7.4):

    selected_grids = all_grids.query('longitude >= {} & longitude <= {} & latitude >= {} & latitude <= {}'
                                     .format(lon_min, lon_max, lat_min, lat_max))

    return selected_grids