from datetime import datetime, timedelta
import pandas as pd

from pandas_dataframes.create_df import csv_to_df


def create_empty_df_with_datetime_index(start, end, timestep):
    """
    Create pandas DateTime index for timeseries data manipulation
    :param start: "YYYY-MM-DD HH:MM:SS" the starting timestamp of the timeseries index
    :param end: "YYYY-MM-DD HH:MM:SS" the last timestamp of the timeseries index
    :param timestep: int: the timestep value in minutes
    :return:
    """
    index = pd.date_range(start=start, end=end, freq='{}min'.format(timestep))
    return pd.DataFrame(index=index)


# print(create_datetime_index(start="2019-09-11 23:30:00", end="2019-09-12 23:30:00", timestep=120))


### extract only hourly data from random timeseries ###
original_ts = csv_to_df('naula_observed.csv', ',')
original_ts['time'] = pd.to_datetime(original_ts['time'], format="%Y-%m-%d %H:%M:%S") # .astype('datetime64')
df = (pd.date_range(start="2019-10-23 23:00:00", end="2019-10-25 10:00:00", freq='60min')).to_frame(name='time')
hourly_ts = pd.merge(df, original_ts, on='time', how='left')
print(hourly_ts)

