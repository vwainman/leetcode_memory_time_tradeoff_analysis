# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
#
#
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
# Example 2:
#
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
#
#
#
from typing import List


class RemoveDuplicatesSolution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.k = 0

    def remove_duplicates(self) -> int:
        # Time: O(n)
        # Memory: O(k)
        if not self.nums:
            return 0

        replace_next = True

        for i, val in enumerate(self.nums[:-1]):
            next_val = self.nums[i+1]
            if replace_next and val != next_val:
                self.k += 1
                self.nums[self.k] = next_val
                replace_next = False
            # non-duplicate encountered, move pointer
            elif val != next_val:
                self.k += 1
            # duplicate encountered, prepare a replacement
            else:
                replace_next = True

        return self.k + 1

    def __eq__(self, other: List[int]):
        for i in range(self.k):
            if self.nums[i] != other[i]:
                return False
        return True

    def __str__(self):
        return str(self.nums[:k])


if __name__ == "__main__":
    case1_input = RemoveDuplicatesSolution([1, 1, 2])
    k: int = case1_input.remove_duplicates()
    case1_output = 2
    assert k == case1_output
    assert case1_input == [1, 2]

    case2_input = RemoveDuplicatesSolution([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    case2_output = 5
    k: int = case2_input.remove_duplicates()
    assert k == case2_output
    print(case2_input)
    assert case2_input == [0, 1, 2, 3, 4]
