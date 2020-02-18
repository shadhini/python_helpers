import pandas as pd
import numpy as np

#########################################
# Distinct Values :: Single Column
#########################################
coefficients = pd.read_csv('sb_rf_coefficients.csv', delimiter=',')

#### iterate through distict values
distinct_names = coefficients.name.unique()
for name in distinct_names:
    print(coefficients[coefficients.name == name])

#### unique values of a column --> dataframe.coulumn_name.unique()
distinct_ids = coefficients.curw_obs_id.unique()

for i in distinct_ids:
    print(i)

#########################################
# Distinct Combinations :: Multiple Column
#########################################

df1 = pd.DataFrame({'A':['yes','yes','yes','yes','no','no','yes','yes','yes','no'],
                   'B':['yes','no','no','no','yes','yes','no','yes','yes','no']})

df1.groupby(['A','B']).size()

df1.groupby(['A','B']).size().reset_index().rename(columns={0:'count'})
