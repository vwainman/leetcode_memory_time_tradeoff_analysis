# https://leetcode.com/problems/3sum/description/
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

from typing import List


def is_prev_duplicate(nums: List[int], i):
    if i > 0:
        return nums[i] == nums[i - 1]
    return False


def adjust_pointers(left_i: int, right_i: int, nums: List[int]):
    while left_i < right_i and nums[left_i] == nums[left_i + 1]:
        left_i += 1
    while left_i < right_i and nums[right_i] == nums[right_i - 1]:
        right_i -= 1
    return (left_i + 1, right_i - 1)


def three_sum(nums: List[int]) -> List[List[int]]:
    """ Sort the nums, traverse and evaluate each index by utilizing a
        double pointer with the next value and the largest (last) value.
        Sum all three, and narrow down a sum closer to zero by moving
        the double pointers according to the summed sign until the double
        pointers collide.
    """
    # Time: O(n^2)
    # Memory: Best O(1), Worst O(n)
    three_sums: List[int] = []
    nums.sort()
    for left_i in range(len(nums) - 2):
        if is_prev_duplicate(nums, left_i):
            continue
        mid_i = left_i + 1
        right_i = len(nums) - 1
        while mid_i < right_i:
            three_sum = nums[left_i] + nums[mid_i] + nums[right_i]
            if three_sum < 0:
                # sum is negative, we need a higher num that will increase it
                mid_i += 1
            elif three_sum > 0:
                # sum is positive, we need a lower num that will decrease it
                right_i -= 1
            else:
                three_sums.append([nums[left_i], nums[mid_i], nums[right_i]])
                # on the same left_i, find any other possible zero sums by
                # adjusting mid_i and right_i to avoid duplicate triplets
                mid_i, right_i = adjust_pointers(mid_i, right_i, nums)
    return three_sums


if __name__ == "__main__":
    case1_input = [-1, 0, 1, 2, -1, -4]
    case1_output = [[-1, -1, 2], [-1, 0, 1]]
    case2_input = []
    case2_output = []
    case3_input = [0]
    case3_output = []
    assert three_sum(case1_input) == case1_output
    assert three_sum(case2_input) == case2_output
    assert three_sum(case3_input) == case3_output
