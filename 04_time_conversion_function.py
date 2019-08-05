# Problem Link - https://www.hackerrank.com/challenges/time-conversion/problem


def time_conversion(time12):
    time24 = time12[2:8]
    am_or_pm = time12[8]
    hour = time12[0:2]

    if am_or_pm == 'A':
        if hour != '12':
            time24 = hour + time24
        else:
            time24 = "00" + time24
    else:
        if hour != '12':
            hr = int(hour) + 12
            time24 = str(hr) + time24
        else:
            time24 = hour + time24
    return time24


print(time_conversion('07:05:45AM'))
print(time_conversion('12:05:45AM'))
print(time_conversion('07:05:45PM'))
print(time_conversion('12:05:45PM'))