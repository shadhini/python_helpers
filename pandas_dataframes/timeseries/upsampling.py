import pandas as pd
from pandas_dataframes.create_df import csv_to_df

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

series = csv_to_df('sample_curw_sim_obs2.csv', ',')
series['time'] = pd.to_datetime(series['time'], format=COMMON_DATE_TIME_FORMAT)
series.set_index('time', inplace=True)

s1 = series.resample('H').asfreq()

print(s1)

# series.resample('30S').pad()
#
# series.resample('30S').bfill()
