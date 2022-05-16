# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
#
# You are given a string time in the form of  hh:mm, where some of the digits
# in the string are hidden (represented by ?).
#
# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden
# digits.

def maximum_time(time: str) -> str:
    latest_valid_time = ""
    hours = time[:2]
    minutes = time[3:]
    if hours == "??":
        latest_valid_time += "23"
    elif hours[0] == "?":
        latest_valid_time += "2" if int(hours[1]) <= 3 else "1"
        latest_valid_time += hours[1]
    elif hours[1] == "?":
        latest_valid_time += hours[0]
        latest_valid_time += "3" if int(hours[0]) == 2 else "9"
    else:
        latest_valid_time += hours
    latest_valid_time += ":"
    if minutes == "??":
        latest_valid_time += "59"
    elif minutes[0] == "?":
        latest_valid_time += "5" + minutes[1]
    elif minutes[1] == "?":
        latest_valid_time += minutes[0] + "9"
    else:
        latest_valid_time += minutes
    return latest_valid_time
