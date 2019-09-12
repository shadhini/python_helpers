import numpy as np
import pandas as pd


def read_csv_to_df(csv_file_name, delimiter, header):
    """
    :param csv_file_name: csv file name: e.g. zoo.csv
    :param delimiter: delimiter used in the csv file to separate columns: e.g. ','
    :param header: header of the dataframe, this is needed in case data file doesn't consists header
    e.g. ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic']
    :return: pandas dataframe containing file content
    """
    if header:
        return pd.read_csv(csv_file_name, delimiter=delimiter, names=header)
    else:
        return pd.read_csv(csv_file_name, delimiter=delimiter)


# !wget 46.101.230.157/dilan/pandas_tutorial_read.csv
df = read_csv_to_df(csv_file_name='/home/shadhini/dev/repos/shadhini/python_helpers/panda_dataframes/pandas_tutorial_read.csv', delimiter=";",
               header=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

# print first few rows of the dataframe
# print(df.head())

# print last few rows of the dataframe
# print(df.tail())

# print random five rows of the dataframe
# print(df.sample(5))

# Select specific columns of your dataframe
# print(df[['country', 'user_id']])

# print series
# print(df.user_id)
# print(df['user_id'])

# Filter for specific values in your dataframe
#print(df[df.source == 'SEO'])

# Slicing dataframe[start_index:end_index:index_step]
# print("*****")
# print(df[:5])
print("*****")
print(df[:11:10])
# print(df)

