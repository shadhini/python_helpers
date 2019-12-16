import pandas as pd
import numpy as np


def csv_to_df(csv_file_name, delimiter, header=None):
    if header is not None:
        return pd.read_csv(csv_file_name, delimiter=delimiter, names=header)
    else:
        return pd.read_csv(csv_file_name, delimiter=delimiter)


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

# print(df)
# print(df['time'].min())

######## merge timeseries ##################
final_merged_df = pd.merge(df, obs, on='time', how='outer')
final_left_merged_df = pd.merge(df, obs, on='time', how='left')
# print(final_left_merged_df)

df1 = final_left_merged_df.copy()
df2 = final_left_merged_df.copy()


###### set multiple indexes ##############
df1['lat'] = 7.741352
df1['lon'] = 80.684432
# print(df1)
df1.set_index(['time', 'lon', 'lat'], inplace=True)

df2['lat'] = 7.741352
df2['lon'] = 80.684432
df2.set_index(['time', 'lon', 'lat'], inplace=True)

# print(df1)
# print(df2)


######## append dataframes ##########
print(df1.append(df2))


