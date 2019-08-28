def join_ts(TS1, TS2):
    """
    Joing time, value pairs of 2 timeseries, if both timeseries include same timestamp,
    :return:
    """

    if TS1[-1][0] > TS2[-1][0]:
        ts1 = TS1
        ts2 = TS2
    else:
        ts1 = TS2
        ts2 = TS1

    output_ts = []

    ts1_index = 0
    ts2_index = 0

    # ts1 last entry has the largest timestamp
    while ts2_index < len(ts2):
        if ts1[ts1_index][0] == ts2[ts2_index][0]:
            output_ts.append(ts1[ts1_index])
            output_ts[-1].append(ts2[ts2_index][1])
            ts1_index += 1
            ts2_index += 1
        elif ts1[ts1_index][0] < ts2[ts2_index][0]:
            output_ts.append(ts1[ts1_index])
            ts1_index += 1
        elif ts1[ts1_index][0] > ts2[ts2_index][0]:
            output_ts.append(ts2[ts2_index])
            ts2_index += 1

    output_ts.extend(ts1[ts1_index:])

    return output_ts


TS1 = [["2019-08-21 23:30:00", 1.2], ["2019-08-22 00:30:00", 1.4], ["2019-08-22 01:00:00", 1.6], ["2019-08-22 01:30:00", 1.4],
       ["2019-08-22 03:00:00", 1.9],["2019-08-22 03:30:00", 1.4],["2019-08-22 04:30:00", 1.4],["2019-08-22 05:30:00", 1.4]]
TS2 = [["2019-08-22 01:30:00", 1.8], ["2019-08-22 02:30:00", 1.5], ["2019-08-22 03:30:00", 1.4],["2019-08-22 07:30:00", 2.4],
       ["2019-08-22 08:30:00", 2.5]]

print(join_ts(TS1,TS2))