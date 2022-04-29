# https://leetcode.com/problems/contains-duplicate/description/
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    # Use a set to determine if a value was repeated in a list
    # Time: O(n)
    # Memory: O(n)
    # Alternatively, we could do len(nums) == len(set(nums)), but
    # the time complexity would always fall on the worst case
    distinct_vals: set = set()
    for val in nums:
        if val in distinct_vals:
            return True
        distinct_vals.add(val)
    return False


if __name__ == "__main__":
    cases = [([1, 2, 3, 1], True),
             ([1, 2, 3, 4], False),
             ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)]
    for input, output in cases:
        assert contains_duplicate(input) == output
