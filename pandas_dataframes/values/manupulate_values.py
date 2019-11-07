import pandas as pd
import numpy as np

coefficients = pd.read_csv('sb_rf_coefficients.csv', delimiter=',')

#### unique values of a column --> dataframe.coulumn_name.unique()
distinct_ids = coefficients.curw_obs_id.unique()

for i in distinct_ids:
    print(i)


#### replace values


