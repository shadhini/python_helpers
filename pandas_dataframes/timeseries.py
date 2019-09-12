from datetime import datetime, timedelta
import pandas as pd


def create_datetime_index(start, end, timestep):
    """
    Create pandas DateTime index for timeseries data manipulation
    :param start: "YYYY-MM-DD HH:MM:SS" the starting timestamp of the timeseries index
    :param end: "YYYY-MM-DD HH:MM:SS" the last timestamp of the timeseries index
    :param timestep: int: the timestep value in minutes
    :return:
    """

    return pd.date_range(start=start, end=end, freq='{}min'.format(timestep))


# print(create_datetime_index(start="2019-09-11 23:30:00", end="2019-09-12 23:30:00", timestep=120))