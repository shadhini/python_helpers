from datetime import datetime, timedelta
import math

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


def round_to_nearest_half_hour(datetime_string, format=None):

    if format is None:
        time = datetime.strptime(datetime_string, COMMON_DATE_TIME_FORMAT)
    else:
        time = datetime.strptime(datetime_string, format)

    if time.minute <= 15:
        return time.strftime("%Y-%m-%d %H:00:00")
    elif (time.minute > 15) and (time.minute < 45):
        return time.strftime("%Y-%m-%d %H:30:00")

    return (time + timedelta(hours=1)).strftime("%Y-%m-%d %H:00:00")


def round_to_nearest_x_minutes(datetime_string, mins, format=None):

    if format is None:
        time = datetime.strptime(datetime_string, COMMON_DATE_TIME_FORMAT)
        format = COMMON_DATE_TIME_FORMAT
    else:
        time = datetime.strptime(datetime_string, format)

    base_time = datetime.strptime(time.strftime("%Y-%m-%d %H:00:00"), format)

    multiplier = round(time.minute / mins)

    return (base_time + timedelta(minutes=mins*multiplier)).strftime(format)


def round_up_datetime_to_nearest_x_minutes(datetime_value, mins):

    base_time = datetime_value.replace(minute=0, second=0, microsecond=0)

    multiplier = math.ceil(datetime_value.minute / mins)

    return base_time + timedelta(minutes=mins*multiplier)


def round_down_datetime_to_nearest_x_minutes(datetime_value, mins):

    base_time = datetime_value.replace(minute=0, second=0, microsecond=0)

    multiplier = math.floor(datetime_value.minute / mins)

    return base_time + timedelta(minutes=mins*multiplier)


# print(round_to_nearest_hour("2019-08-30 08:15:00"))

# print(round_to_nearest_half_hour("2019-08-30 23:58:00"))

# print(round_to_nearest_x_minutes("2019-08-30 08:16:00", 15))

# print(type(datetime.now()))
#
# time = datetime.strptime("2019-10-05 23:45:00", COMMON_DATE_TIME_FORMAT)
#
# print(round_up_datetime_to_nearest_x_minutes(time, 15))
# print(round_down_datetime_to_nearest_x_minutes(time, 15))


### UTC time
def get_SL_time_now():
    return  (datetime.utcnow() + timedelta(hours=5, minutes=30))





