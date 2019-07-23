from datetime import datetime, timedelta

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def now_as_string(string_format=None):
    if string_format is None:
        return datetime.now().strftime(COMMON_DATE_TIME_FORMAT)
    else:
        return datetime.now().strptime(string_format)


def now_as_datetime(format=None):
    if format is None:
        return datetime.now()
    else:
        return datetime.strptime(datetime.now().strftime(format), format)


def datetime_to_str(datetime_value, string_format=None):
    if format is None:
        return datetime_value.strftime(COMMON_DATE_TIME_FORMAT)
    else:
        return datetime_value.strftime(string_format)


def str_to_datetime(datetime_string, format=None):
    if format is None:
        datetime.strptime(datetime_string, COMMON_DATE_TIME_FORMAT)
    else:
        datetime.strptime(datetime_string, format)


