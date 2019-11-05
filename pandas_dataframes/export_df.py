import pandas as pd

###### save to file ###############
df = pd.DataFrame()
pd.to_csv("file_name.txt", columns=['value'], header=False, index=None)

###### pandas df to list of lists #####
df.reset_index().values.tolist()