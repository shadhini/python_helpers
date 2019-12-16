import pandas as pd

df = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})

##### min max values of column #####
print(df['A'].min())
print(df['B'].max())

##### max max values of row #####
df['min'] = df.min(axis=1)
df['max'] = df.max(axis=1)

print(df)
