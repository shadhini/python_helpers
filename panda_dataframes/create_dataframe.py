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





