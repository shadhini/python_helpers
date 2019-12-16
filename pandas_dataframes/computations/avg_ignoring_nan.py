import pandas as pd
import numpy as np

#### average along  a row ignoring NaN
df = pd.DataFrame({'a': [1, 5, 9, np.nan], 'b': [9, np.nan, 55, 4], 'c': [5, 4, np.nan, 9]})
df_mean = df.mean(axis=1)
print(df_mean)