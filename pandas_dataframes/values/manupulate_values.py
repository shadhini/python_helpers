import pandas as pd
import numpy as np

coefficients = pd.read_csv('sb_rf_coefficients.csv', delimiter=',')

#### iterate through distict values
distinct_names = coefficients.name.unique()
for name in distinct_names:
    print(coefficients[coefficients.name == name])
#### unique values of a column --> dataframe.coulumn_name.unique()
# distinct_ids = coefficients.curw_obs_id.unique()
#
# for i in distinct_ids:
#     print(i)


#### replace values_
# curw_sim = pd.read_csv('sample_curw_sim_obs.csv', delimiter=',')
# curw_sim_value_replaced_by_value = curw_sim.replace(to_replace=-99999.0, value=100)
#
# curw_sim_negative_replaced_by_nan = curw_sim
# num = curw_sim_negative_replaced_by_nan._get_numeric_data()
# num[num < 0] = np.nan
# # curw_sim_negative_replaced_by_nan = curw_sim[curw_sim < 0] = np.nan
#
# print(curw_sim_negative_replaced_by_nan)


#### average along  a row ignoring NaN
df = pd.DataFrame({'a': [1, 5, 9, np.nan], 'b': [9, np.nan, 55, 4], 'c': [5, 4, np.nan, 9]})
# print(df)
# df_mean = df.mean(axis=1)
# print(df_mean)

#### replacing nan with row average
# m = df.mean(axis=1)
# for i, col in enumerate(df):
#  # using i allows for duplicate columns
#  # inplace *may* not always work here, so IMO the next line is preferred
#  # df.iloc[:, i].fillna(m, inplace=True)
#  df.iloc[:, i] = df.iloc[:, i].fillna(m)

# print(df)
#
#
# def replace_negative_numbers_with_nan(df):
#     num = df._get_numeric_data()
#     num[num < 0] = np.nan
#     return df
#
#
# def replace_nan_with_row_average(df):
#     m = df.mean(axis=1)
#     for i, col in enumerate(df):
#         df.iloc[:, i] = df.iloc[:, i].fillna(m)
#     return df
#
#
# print(replace_negative_numbers_with_nan(df))
# print(replace_nan_with_row_average(df))