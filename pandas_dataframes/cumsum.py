import pandas as pd

df = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})
print(df)

# cum sum along columns
df1 = df.cumsum(axis = 0)
print(df1)

# cum sum along rows
df2 = df.cumsum(axis = 1)
print(df2)

# cum sum of particular column along the col
a = df['A'].cumsum()
print(a)