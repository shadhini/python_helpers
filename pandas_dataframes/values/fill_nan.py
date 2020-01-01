import pandas as pd

df = pd.DataFrame()

print (df)
#                          A         B
# DateTime
# 01-01-2017 03:27       NaN       NaN
# 01-01-2017 03:28       NaN       NaN
# 01-01-2017 03:29  0.181277 -0.178836
# 01-01-2017 03:30  0.186923 -0.183261
# 01-01-2017 03:31       NaN       NaN
# 01-01-2017 03:32       NaN       NaN
# 01-01-2017 03:33  0.181277 -0.178836

data = df.ffill().bfill()
print (data)

#                         A         B
# DateTime
# 01-01-2017 03:27  0.181277 -0.178836
# 01-01-2017 03:28  0.181277 -0.178836
# 01-01-2017 03:29  0.181277 -0.178836
# 01-01-2017 03:30  0.186923 -0.183261
# 01-01-2017 03:31  0.186923 -0.183261
# 01-01-2017 03:32  0.186923 -0.183261
# 01-01-2017 03:33  0.181277 -0.178836
# Which is same as the function fillna with parameters:

data = df.fillna(method='ffill').fillna(method='bfill')