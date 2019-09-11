from datetime import datetime, timedelta
import numpy as np
import pandas as pd

#====================================
# date_time_index = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), datetime(2018, 1, 1)])
# works

#date_time_index = pd.to_datetime(['1/1/2018 23:59:59', '2019-12-30 23:59:59', np.datetime64('2018-01-01 23:59:59'), datetime(2018, 1, 1, 23, 59, 59)])
# works

#print(date_time_index)
#====================================

date_time_index = pd.date_range(start="2019-09-11 23:30:00", end="2019-09-12 23:30:00", freq='120min')

print(date_time_index)