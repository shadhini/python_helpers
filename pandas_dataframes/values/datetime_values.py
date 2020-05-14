import pandas as pd

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

df = pd.DataFrame()

# convert datetime column to string type
df['time'] = df['time'].dt.strftime('%Y-%m-%d')

# convert string column to datetime type
df['time'] = pd.to_datetime(df['time'], format=COMMON_DATE_TIME_FORMAT)

# convert datetime index to string type
df.set_index('time', inplace=True)
final_df = df['final'].reset_index()
final_df['time'] = final_df['time'].dt.strftime(COMMON_DATE_TIME_FORMAT)
final_ts = final_df.values.tolist()