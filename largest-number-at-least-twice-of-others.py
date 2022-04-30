# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much
# as every other number in the array. If it is, return the index of the largest
# element, or return -1 otherwise.
#

from typing import List


def max_and_index(nums: List[int]) -> tuple:
    max_num, index = nums[0], 0
    for i, num in enumerate(nums[1:]):
        if num > max_num:
            max_num, index = num, i + 1
    return max_num, index


def dominant_index(nums: List[int]) -> int:
    # Time: O(n)
    # Space: O(1)
    if len(nums) == 1:
        return 0
    second_largest_num = min(nums[0], nums[1])
    max_num, max_num_index = max_and_index(nums[:2])
    for i, num in enumerate(nums[2:]):
        if num > max_num:
            second_largest_num = max_num
            max_num, max_num_index = num, i + 2
        elif num > second_largest_num:
            second_largest_num = num
    if second_largest_num * 2 <= max_num:
        return max_num_index
    return -1


if __name__ == "__main__":
    case_inputs = [[3, 6, 1, 0], [1, 2, 3, 4], [1], [0, 0, 0, 1], [0, 0, 3, 2]]
    case_outputs = [1, -1, 0, 3, -1]
    for case_input, case_output in zip(case_inputs, case_outputs):
        assert dominant_index(case_input) == case_output
