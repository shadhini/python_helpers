import os
import time
from datetime import datetime, timedelta


def get_file_last_modified_time_offset_5_30(file_path):
    # os.path.getmtime() returns modified time as seconds since the epoch
    # time.gmtime() converts seconds since the epoch	time.struct_time in UTC
    # time.localtime() converts seconds since the epoch	time.struct_time in localime

    # returns local time (UTC + 5 30)
    modified_time = time.gmtime(os.path.getmtime(file_path) + 19800)

    return time.strftime('%Y-%m-%d %H:%M:%S', modified_time)


def get_file_last_modified_time_SL(file_path):

    modified_time_raw = os.path.getmtime(file_path)
    print("modified_time_raw: ", modified_time_raw)

    modified_time_utc = datetime.utcfromtimestamp(modified_time_raw)
    print("modified_time_utc: ", modified_time_utc)

    # # returns local time (UTC + 5 30)
    modified_time_SL = modified_time_utc + timedelta(hours=5, minutes=30)

    return modified_time_SL.strftime('%Y-%m-%d %H:%M:%S')

print(get_file_last_modified_time_SL("/home/shadhini/dev/repos/shadhini/python_helpers/file_utils/test_file.txt"))