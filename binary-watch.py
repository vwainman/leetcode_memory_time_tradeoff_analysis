# https://leetcode.com/problems/binary-watch/description/
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a
# zero or one, with the least significant bit on the right.
#
# For example, the below binary watch reads "4:51".
#
# H    8  [4] 2 1    [PM]
# M [32] [16] 8 4 [2] [1]
#
# Given an integer turned_on which represents the number of LEDs that are
# currently on, return all possible times the watch could represent. You may
# return the answer in any order.
#
# The hour must not contain a leading zero.
#
# For example, "01:00" is not valid. It should be "1:00".
#
# The minute must be consist of two digits and may contain a leading
# zero.
#
# For example, "10:2" is not valid. It should be "10:02".
#
# Example 1:
# Input: turnedOn = 1
# Output:
# ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:
# Input: turnedOn = 9
# Output: []
#
#
# Constraints:
#
#
# 0 <= turnedOn <= 10
#
#
#

from typing import List


def read_binary_watch(turned_on: int) -> List[str]:
    # Time: O(n_hours * m_mins)
    # Memory: O(n_permutations)
    if turned_on <= 0 or turned_on > 8:
        return []
    LED_ON: str = '1'
    possible_times = []
    for hours in range(12):
        for minutes in range(60):
            if str(bin(hours) + bin(minutes)).count(LED_ON) == turned_on:
                possible_times.append(f"{hours}:{minutes:02d}")
    return possible_times


if __name__ == "__main__":
    assert read_binary_watch(1) == [
        "0:01", "0:02", "0:04", "0:08", "0:16",
        "0:32", "1:00", "2:00", "4:00", "8:00"]
    assert read_binary_watch(9) == []
