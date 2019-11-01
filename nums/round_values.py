def round_to_last_hundred(number):
    factor = (number // 100)
    return factor * 100

print(round_to_last_hundred(9300))