import pandas as pd

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

df = pd.DataFrame()

# convert datetime column to string type
df['time'] = df['time'].dt.strftime('%Y-%m-%d')

# convert string column to datetime type
df['time'] = pd.to_datetime(df['time'], format=COMMON_DATE_TIME_FORMAT)