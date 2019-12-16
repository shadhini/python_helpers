import pandas as pd
import numpy as np

coefficients = pd.read_csv('sb_rf_coefficients.csv', delimiter=',')

#### iterate through distict values
distinct_names = coefficients.name.unique()
for name in distinct_names:
    print(coefficients[coefficients.name == name])

#### unique values of a column --> dataframe.coulumn_name.unique()
distinct_ids = coefficients.curw_obs_id.unique()

for i in distinct_ids:
    print(i)
