import pandas as pd

df = pd.DataFrame()

df.sort_values(['longitude', 'latitude'], ascending=[True, True])
df.sort_index(inplace=True)