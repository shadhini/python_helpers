import pandas as pd

from pandas_dataframes.create_df import csv_to_df

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


obs_5min_ts = csv_to_df('sample_curw_sim_obs.csv', ',')
obs_5min_ts['time'] = pd.to_datetime(obs_5min_ts['time'], format=COMMON_DATE_TIME_FORMAT)
obs_5min_ts.set_index('time', inplace=True)
print(obs_5min_ts)

min15_ts = pd.DataFrame()
min15_ts['value'] = obs_5min_ts['value'].resample('15min', label='right', closed='right').sum()

print(min15_ts)

# min15_ts['value'].resample('3T', label='left', closed='left', loffset='2T').sum()

"""
open and closed in this setting is about strict vs non-strict inequality (e.g. < vs <=).

An example should make this clear. Using an interior interval from your example, this is the difference from changing the value of closed:

closed='right' =>  ( 3:00, 6:00 ]  or  3:00 <  x <= 6:00
closed='left'  =>  [ 3:00, 6:00 )  or  3:00 <= x <  6:00



The label parameter merely controls whether the left (3:00) or right (6:00) side is displayed, but doesn't impact the results themselves.

Also note that you can change the starting point for the intervals with the loffset parameter (which should be entered as a time delta).




"""