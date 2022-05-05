# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: "TreeNode"):
        # root to depth comparison
        if not self and not other:
            return True
        elif self and other:
            if self.val != other.val:
                return False
            return self.left.__eq__(other.left) \
                and self.right.__eq__(other.right)
        else:
            return False


def sorted_array_to_bin_search_tree_recursive(nums: List[int]) -> Optional[TreeNode]:
    # Time: O(n)
    # Space: O(n)
    if not nums:
        return None
    root_i = len(nums) // 2
    root = TreeNode(nums[root_i])
    left = nums[:root_i]
    right = nums[root_i + 1:]
    root.left = sorted_array_to_bin_search_tree_recursive(left)
    root.right = sorted_array_to_bin_search_tree_recursive(right)
    return root


def sorted_array_to_bin_search_tree_iterative(nums: List[int]) -> Optional[TreeNode]:
    # Time: O(n)
    # Space: O(n)
    root_i = len(nums) // 2
    root = TreeNode(nums[root_i])
    left = nums[:root_i]
    right = nums[root_i + 1:]
    queue = [(root, left, right)]  # FIFO
    while queue:
        head, left, right = queue.pop(0)
        if left:
            head_i = len(left) // 2
            head.left = TreeNode(left[head_i])
            left_left = left[:head_i]
            left_right = left[head_i + 1:]
            queue.append((head.left, left_left, left_right))
        if right:
            head_i = len(right) // 2
            head.right = TreeNode(right[head_i])
            right_left = right[:head_i]
            right_right = right[head_i+1:]
            queue.append((head.right, right_left, right_right))
    return root


if __name__ == "__main__":
    case1_input = [-10, -3, 0, 5, 9]
    case1_output = TreeNode(
        0, TreeNode(-3, TreeNode(-10), None), TreeNode(9, TreeNode(5), None))
    for function in [sorted_array_to_bin_search_tree_iterative,
                     sorted_array_to_bin_search_tree_recursive]:
        assert function(case1_input) == case1_output
