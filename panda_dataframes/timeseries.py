from datetime import datetime, timedelta
import pandas as pd


def create_datetime_index(start, end, timestep):
    """
    Create pandas DateTime index for timeseries data manipulation
    :param start: the starting timestamp of the timeseries index
    :param end: the last timestamp of the timeseries index
    :param timestep: the timestep value in minutes
    :return:
    """

