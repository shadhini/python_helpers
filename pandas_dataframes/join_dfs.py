import pandas as pd
import numpy as np


def create_empty_df_with_datetime_index(start, end, timestep):
    index = pd.date_range(start=start, end=end, freq='{}min'.format(timestep))
    return pd.DataFrame(index=index)


def list_of_lists_to_df_first_column_as_index(data):
    original_data = np.array(data)
    index = original_data[:, 0]
    data = original_data[:, 1:]

    return pd.DataFrame.from_records(data=data, index=index)


def ts_linear_interpolation(dataframe, interpolation_method):

    new_dataframe = pd.to_numeric(dataframe[dataframe.columns[0]], errors='coerce')
    return new_dataframe.interpolate(method=interpolation_method, limit_direction='both')


TS2 = [["2019-08-22 01:00:00", 1.8], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4],["2019-08-22 07:30:00", 2.4],
       ["2019-08-22 08:30:00", 2.5], ["2019-08-23 07:30:00", 2.5], ["2019-08-23 08:30:00", 2.5]]

time_index = create_empty_df_with_datetime_index(start="2019-08-22 00:00:00", end="2019-08-23 12:00:00", timestep=5)

timeseries = list_of_lists_to_df_first_column_as_index(data=TS2)

# print(time_index)
# print(timeseries)

# print(time_index)
# print(timeseries.index)

# Left Join (left.join(right))
continuous_ts = time_index.join(timeseries)
# continuous_ts = time_index.join(timeseries, lsuffix='_left', rsuffix='_right') # with suffixes in case of conflicting columns
interpolated_ts = ts_linear_interpolation(dataframe=continuous_ts, interpolation_method='linear')

print(interpolated_ts)

