def extract_ts_from(start_date, timeseries):
    """
    timeseries from start date (inclusive)
    :param start_date:
    :param timeseries:
    :return:
    """

    output_ts = []

    for i in range(len(timeseries)):
        if timeseries[i][0] >= start_date:
            output_ts = timeseries[i:]
            break

    return output_ts


def extract_ts_till(end_date, timeseries):
    """
    timeseries till end date (exclusive)
    :param end_date:
    :param timeseries:
    :return:
    """
    output_ts = []

    for i in range(len(timeseries)):
        if timeseries[i][0] >= end_date:
            output_ts = timeseries[0:i]
            break

    return output_ts


def extract_from_to(start_date, end_date, timeseries):

    """
    timeseries from start date (inclusive) to end date (exclusive)
    :param start_date:
    :param end_date:
    :param timeseries:
    :return:
    """

    start_index = 0
    end_index = 0

    for i in range(len(timeseries)):
        if timeseries[i][0] >= start_date:
            start_index = i
            break

    for i in range(len(timeseries)):
        if timeseries[i][0] >= end_date:
            end_index = i
            break

    return timeseries[start_index: end_index]


original = [['2019-08-21 23:30:00', 1.2], ['2019-08-22 00:30:00', 1.4], ['2019-08-22 01:00:00', 1.6],
                ['2019-08-22 01:30:00', 1.8, 1.4], ['2019-08-22 02:30:00', 1.5], ['2019-08-22 03:00:00', 1.9],
                ['2019-08-22 03:30:00', 1.4, 1.4], ['2019-08-22 04:30:00', 1.4], ['2019-08-22 05:30:00', 1.4],
                ['2019-08-22 07:30:00', 2.4], ['2019-08-22 08:30:00', 2.5]]

print(extract_ts_till(end_date="2019-08-22 07:31:00", timeseries=original))