# https://leetcode.com/problems/next-permutation/description/
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
#
# For example, for arr = [1,2,3], the following are considered permutations of
# arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
#
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
#
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.

from typing import List


def next_permutation(nums: List[int]) -> None:
    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    if n == 1:
        return
    index = n - 1
    # reverse search for a adjacent-left value to be smaller than the next
    while index > 0 and nums[index - 1] >= nums[index]:
        index -= 1
    # if one isn't found, we sort ascendingly in-place
    if index == 0:
        nums.sort()
        return
    # otherwise, find the index to swap with
    else:
        j = n - 1
        # reverse search for an index with
        # a value greater than the adjacent value
        while(j >= index and nums[index - 1] >= nums[j]):
            j -= 1
        # swap the correct indices values
        nums[j], nums[index - 1] = nums[index - 1], nums[j]
        # minimize the larger part by reversely sorting
        nums[index:].sort(reverse=True)
        return


if __name__ == "__main__":
    case1_input = [1, 2, 3]
    case2_input = [3, 2, 1]
    case3_input = [1, 1, 5]
    case1_inplace = [1, 3, 2]
    case2_inplace = [1, 2, 3]
    case3_inplace = [1, 5, 1]
    next_permutation(case1_input)
    assert case1_input == case1_inplace
    next_permutation(case2_input)
    assert case2_input == case2_inplace
    next_permutation(case3_input)
    assert case3_input == case3_inplace
