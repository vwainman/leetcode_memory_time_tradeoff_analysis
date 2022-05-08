# https://leetcode.com/problems/happy-number/description/
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.

def is_happy(n: int) -> bool:
    # Time: O(n)
    # Space: O(n)
    applied_nums = set()
    while n != 1:
        n = sum([int(digit) * int(digit) for digit in str(n)])
        if n in applied_nums:
            return False
        applied_nums.add(n)
    return True


if __name__ == "__main__":
    case1_input = 19
    case1_output = True
    case2_input = 2
    case2_output = False
    assert is_happy(case1_input) == case1_output
    assert is_happy(case2_input) == case2_output
