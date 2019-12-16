import pandas as pd
import numpy as np


df = pd.DataFrame({'a': [1, 5, 9, np.nan], 'b': [9, np.nan, 55, 4], 'c': [5, 4, np.nan, 9]})


def replace_negative_numbers_with_nan(df):
    num = df._get_numeric_data()
    num[num < 0] = np.nan
    return df


print(replace_negative_numbers_with_nan(df))
