# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
#
# Example 2:
#
#
# Input: root = [1,null,2]
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
#
#
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_depth(node: Optional[TreeNode], current_depth: int = 1) -> int:
    if node is None:
        return current_depth
    current_depth += 1
    return max(leaf_depth(node.left, current_depth),
               leaf_depth(node.right, current_depth))


def max_depth(root: Optional[TreeNode]) -> int:
    # Time: O(n - number of nodes)
    # Memory: O(n - number of nodes)
    # utilizes a top-bottom depth-first search
    if root is None:
        return 0
    return max(leaf_depth(root.left), leaf_depth(root.right))


if __name__ == "__main__":
    case1_input = TreeNode(3, TreeNode(
        9), TreeNode(20, TreeNode(15), TreeNode(7)))
    case2_input = TreeNode(1, None, TreeNode(2))
    assert max_depth(case1_input) == 3
    assert max_depth(case2_input) == 2
