# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class SearchInsertSolution:

    def __init__(self, nums: List[int], target: int):
        self.nums = nums
        self.target = target
        self.validate_args()

    def validate_args(self):
        if 1 > len(self.nums) > 10**4:
            raise Exception("length of num out of bounds")
        for val in self.nums:
            if -10**4 > val > 10**4:
                raise Exception("value of num index out of bounds")
        if -10**4 > self.target > 10**4:
            raise Exception("value of target out of bounds")

    def exhaustive_search(self) -> int:
        # Initial approach
        # Time: O(n), not good enough
        # Memory: O(1)
        for i, val in enumerate(self.nums):
            if val == self.target:
                return i
            elif val > self.target:
                return i
            elif i == 0 and self.target < val:
                return 0
        return len(self.nums)

    def binary_search(self) -> int:
        # Time: O(log n)
        # Memory: O(1)
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if self.nums[mid] >= self.target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    case1_input = SearchInsertSolution([1, 3, 5, 6], 5)
    case1_output = 2
    case2_input = SearchInsertSolution([1, 3, 5, 6], 2)
    case2_output = 1
    case3_input = SearchInsertSolution([1, 3, 5, 6], 7)
    case3_output = 4
    case4_input = SearchInsertSolution([1, 3, 5, 6], 0)
    case4_output = 0
    assert case1_input.exhaustive_search() == case1_output
    assert case2_input.exhaustive_search() == case2_output
    assert case3_input.exhaustive_search() == case3_output
    assert case4_input.exhaustive_search() == case4_output
    assert case1_input.binary_search() == case1_output
    assert case2_input.binary_search() == case2_output
    assert case3_input.binary_search() == case3_output
    assert case4_input.binary_search() == case4_output
