import pandas as pd
import numpy as np


curw_sim = pd.read_csv('sample_curw_sim_obs.csv', delimiter=',')

#### replace values_
# replace with value
curw_sim_value_replaced_by_value = curw_sim.copy().replace(to_replace=-99999.0, value=100)

## replace with NaN under condition
curw_sim_numeric = curw_sim._get_numeric_data()
curw_sim_numeric[curw_sim_numeric < 0] = np.nan

curw_sim_negative_replaced_by_nan = curw_sim_numeric


print(curw_sim_negative_replaced_by_nan)