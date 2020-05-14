# https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13a1ea037f7
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.array([[1, 2, 3], [np.nan, 4, 6], [np.nan, 6, 9], [np.nan, np.nan, 12], [np.nan, np.nan, np.nan]]),
    columns=['a', 'b', 'c']
)

print(df)


def func(a, b, c):
    if np.isnan(a):
        if np.isnan(b):
            return c
        else:
            return b
    else:
        return a


df['final'] = df.apply(
    lambda row: func(row['a'], row['b'], row['c']), axis=1
)

print(df)