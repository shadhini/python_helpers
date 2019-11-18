import pandas as pd

###### save to file ###############
df = pd.DataFrame()
df.to_csv("file_name.txt", columns=['value'], header=True, index=True)

###### pandas df to list of lists #####
df.reset_index().values.tolist()  # including index
df.values.tolist()  # excluding index