import pandas as pd


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

