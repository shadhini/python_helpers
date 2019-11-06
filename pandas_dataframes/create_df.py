import pandas as pd
import numpy as np


def csv_to_df(csv_file_name, delimiter, header=None):
    """
    :param csv_file_name: csv file name: e.g. zoo.csv
    :param delimiter: delimiter used in the csv file to separate columns: e.g. ','
    :param header: header of the dataframe, this is needed in case data file doesn't consists header
    e.g. ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic']
    :return: pandas dataframe containing file content
    """
    if header is not None:
        return pd.read_csv(csv_file_name, delimiter=delimiter, names=header)
    else:
        return pd.read_csv(csv_file_name, delimiter=delimiter)


def list_of_lists_to_df(data, index=None, columns=None):
    """

    :param data: data in list of lists format
    :param index: array like series that should be considered as the index
    :param columns: list of column names
    :return: equivalent pandas dataframe
    """

    return pd.DataFrame.from_records(data, index=index, columns=columns)


def list_of_lists_to_df_first_row_as_columns(data):
    """

    :param data: data in list of lists format
    :return: equivalent pandas dataframe
    """

    return pd.DataFrame.from_records(data[1:], columns=data[0])


def list_of_lists_to_df_first_row_as_columns_first_column_as_index(data):
    """

    :param data: data in list of lists format
    :return: equivalent pandas dataframe
    """
    original_data = np.array(data)
    columns = original_data[0, 1:]
    index = original_data[1:, 0]
    data = original_data[1:, 1:]

    return pd.DataFrame.from_records(data=data, columns=columns, index=index)


def list_of_lists_to_df_first_column_as_index(data):
    """

    :param data: data in list of lists format
    :return: equivalent pandas dataframe
    """
    original_data = np.array(data)
    index = original_data[:, 0]
    data = original_data[:, 1:]

    # datetime_index = index.astype('datetime64', copy=False)

    return pd.DataFrame.from_records(data=data, index=index)


TS2 = [["time", "value"], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4],["2019-08-22 07:30:00", 2.4],
       ["2019-08-22 08:30:00", 2.5], ["2019-08-23 07:30:00", 2.5], ["2019-08-23 08:30:00", 2.5]]

TS1 = [["2019-08-22 01:30:00", 1.8], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4]]

# print(list_of_lists_to_df(data=TS2))

# TS2 = np.array(TS2)
# print(TS2[0, 1:])
# print(TS2[1:,1:])

# print(list_of_lists_to_df_first_row_as_columns_first_column_as_index(data=TS2))


# print(list_of_lists_to_df_first_column_as_index(data=TS2))
