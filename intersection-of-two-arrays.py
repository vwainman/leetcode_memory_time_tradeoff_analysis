# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

from typing import List


def intersection_set_comparison(nums1: List[int], nums2: List[int]) -> List[int]:
    # use a set for one array to determine intersecting elements of the other array
    # Time: O(n + m) where n = len(nums1) and m = len(nums2)
    # Space: O(n)
    nums1_set = set(nums1)
    return list({num for num in nums2 if num in nums1_set})


if __name__ == "__main__":
    case1_inputs = [[1, 2, 2, 1], [2, 2]]
    case1_output = [2]
    case2_inputs = [[4, 9, 5], [9, 4, 9, 8, 4]]
    case2_output = [9, 4]
    assert intersection_set_comparison(*case1_inputs) == case1_output
    assert intersection_set_comparison(*case2_inputs) == case2_output
