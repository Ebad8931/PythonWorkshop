# Getting input
time12 = input("Enter time in hh:mm:ssAM or hh:mm:ssPM ")
# time12 and time24 have common minutes and seconds [:mm:ss]
time24 = time12[2:8]
# str12 format: hh:mm:ssAM or hh:mm:ssPM
am_or_pm = time12[8]
# Slicing hours
hour = time12[0:2]

if am_or_pm == 'A':
    # for str12 01:00AM to 11:59AM
    if hour != '12':
        time24 = hour + time24
    # for str12 12:00AM to 12:59AM
    else:
        time24 = "00" + time24
else:
    # for str12 01:00PM to 11:59PM
    if hour != '12':
        hr = int(hour) + 12
        time24 = str(hr) + time24
    # for str12 12:00PM to 12:59PM
    else:
        time24 = hour + time24

print('Time in 24-hour clock format:', time24)
