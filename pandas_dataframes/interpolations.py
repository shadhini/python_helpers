import pandas as pd
from datetime import datetime, timedelta


def ts_linear_interpolation(dataframe, interpolation_method):
    """

    :param interpolation_method:
    :return:
    """

    new_dataframe = pd.to_numeric(dataframe[dataframe.columns[0]], errors='coerce')
    return new_dataframe.interpolate(method=interpolation_method, limit_direction='both')

