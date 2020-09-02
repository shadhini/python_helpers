import pandas as pd
import numpy as np

# df = pd.DataFrame(
#     np.array([[1, 2, 3], [4, 5, np.nan], [7, 8, 9], [3, 2, np.nan], [5, 6, np.nan]]),
#     columns=['a', 'b', 'c']
# )
#
# print(df)
#
# df['c'] = df.apply(
#     lambda row: row['a']*row['b'] if np.isnan(row['c']) else row['c'],
#     axis=1
# )
#
# print(df)

df = pd.DataFrame(
    np.array([[1, 2, 3], [np.nan, 4, 6], [np.nan, 6, 9], [np.nan, np.nan, 12], [np.nan, np.nan, np.nan]]),
    columns=['a', 'b', 'c']
)

print(df)

# df['Cat1'].fillna(df['Cat2'])

df['b'] = df['b'].fillna(df['c'])
df['a'] = df['a'].fillna(df['b'])

# for col in df.columns:
#     df[col] = df[col].fillna(df['b'])

print(df)