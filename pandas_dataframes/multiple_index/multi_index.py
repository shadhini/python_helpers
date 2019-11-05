import pandas as pd
import numpy as np

from pandas_dataframes.create_dataframe import  csv_to_df


WRF_A = csv_to_df('naula_fcst_WRF_A_d0_18.csv', ',')
WRF_C = csv_to_df('naula_fcst_WRF_C_d0_18.csv', ',')
WRF_E = csv_to_df('naula_fcst_WRF_E_d0_18.csv', ',')
WRF_SE = csv_to_df('naula_fcst_WRF_SE_d0_18.csv', ',')
obs = csv_to_df('naula_observed.csv', ',')

# WRF_A['lat'] = 7.741352
# WRF_A['lon'] = 80.684432

forecast_list = [WRF_A, WRF_C, WRF_E, WRF_SE]

df = pd.DataFrame()
df_initialized = False

# set multiple indexes
# WRF_A.set_index(['time', 'lon', 'lat'], inplace=True)

for fcst in forecast_list:
    if not df_initialized:
        df = fcst
        df_initialized = True
    else:
        df = pd.merge(df, fcst, on='time', how='outer')

print(df)
print(df['time'].min())

