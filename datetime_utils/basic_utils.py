from datetime import datetime, timedelta

COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def now_as_string(string_format=None):
    if string_format is None:
        return datetime.now().strftime(COMMON_DATE_TIME_FORMAT)
    else:
        return datetime.now().strftime(string_format)


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


def round_to_nearest_hour(datetime_string, format=None):

    if format is None:
        time = datetime.strptime(datetime_string, COMMON_DATE_TIME_FORMAT)
    else:
        time = datetime.strptime(datetime_string, format)

    if time.minute > 30:
        return (time + timedelta(hours=1)).strftime("%Y-%m-%d %H:00:00")

    return time.strftime("%Y-%m-%d %H:00:00")


print(round_to_nearest_hour("2019-08-30 08:29:00"))



