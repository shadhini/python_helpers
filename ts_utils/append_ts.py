def append_ts(original_ts, new_ts):
    """
    append new ts to original ts
    :param original_ts:
    :param new_ts:
    :return:
    """

    appended_ts = []

    original_ts_index = 0
    new_ts_index = 0

    while original_ts_index < len(original_ts):

        if new_ts_index < len(new_ts):

            if original_ts[original_ts_index][0] == new_ts[new_ts_index][0]:
                appended_ts.append(original_ts[original_ts_index])
                appended_ts[original_ts_index].append(new_ts[new_ts_index][1])
                original_ts_index += 1
                new_ts_index += 1
            elif original_ts[original_ts_index][0] < new_ts[new_ts_index][0]:
                appended_ts.append(original_ts[original_ts_index])
                original_ts_index += 1
            elif original_ts[original_ts_index][0] > new_ts[new_ts_index][0]:
                appended_ts.append(new_ts[new_ts_index])
                new_ts_index += 1
        else:
            if original_ts_index < len(original_ts):
                appended_ts.extend(original_ts[original_ts_index:])
            break

    if new_ts_index < len(new_ts):
        appended_ts.extend(new_ts[new_ts_index:])

    return appended_ts


original = [['2019-08-21 23:30:00', 1.2], ['2019-08-22 00:30:00', 1.4], ['2019-08-22 01:00:00', 1.6], ['2019-08-22 01:30:00', 1.8, 1.4], ['2019-08-22 02:30:00', 1.5], ['2019-08-22 03:00:00', 1.9], ['2019-08-22 03:30:00', 1.4, 1.4], ['2019-08-22 04:30:00', 1.4], ['2019-08-22 05:30:00', 1.4], ['2019-08-22 07:30:00', 2.4], ['2019-08-22 08:30:00', 2.5]]

TS2 = [["2019-08-22 01:30:00", 1.8], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4],["2019-08-22 07:30:00", 2.4],
       ["2019-08-22 08:30:00", 2.5], ["2019-08-23 07:30:00", 2.5], ["2019-08-23 08:30:00", 2.5]]

TS1 = [["2019-08-22 01:30:00", 1.8], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4]]

TS3 = [['2019-08-19 00:30:00', 9.4]]

TS4 = []

print(append_ts(original, TS4))

