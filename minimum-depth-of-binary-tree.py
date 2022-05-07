# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]):
    if not root:
        return 0
    if not root.left or not root.right:
        # missing child(s) node
        return max(min_depth(root.left), min_depth(root.right)) + 1
    else:
        # parent node
        return min(min_depth(root.left), min_depth(root.right)) + 1


if __name__ == "__main__":
    case1_input = TreeNode(2, TreeNode(9, None, None),
                           TreeNode(20, TreeNode(15), TreeNode(7)))
    case1_output = 2
    case2_input = TreeNode(2, None, TreeNode(
        3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    case2_output = 5

    for function in [min_depth]:
        assert function(case1_input) == case1_output
        assert function(case2_input) == case2_output
