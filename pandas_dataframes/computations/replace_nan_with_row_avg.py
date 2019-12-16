import pandas as pd
import numpy as np


df = pd.DataFrame({'a': [1, 5, 9, np.nan], 'b': [9, np.nan, 55, 4], 'c': [5, 4, np.nan, 9]})


#### replacing nan with row average
m = df.mean(axis=1)
for i, col in enumerate(df):
 # using i allows for duplicate columns
 # inplace *may* not always work here, so IMO the next line is preferred
 # df.iloc[:, i].fillna(m, inplace=True)
 df.iloc[:, i] = df.iloc[:, i].fillna(m)

print(df)


def replace_nan_with_row_average(df):
    m = df.mean(axis=1)
    for i, col in enumerate(df):
        df.iloc[:, i] = df.iloc[:, i].fillna(m)
    return df


print(replace_nan_with_row_average(df))