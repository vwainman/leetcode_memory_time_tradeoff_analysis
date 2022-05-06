# https://leetcode.com/problems/balanced-binary-tree/description/
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced_recursive(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def preorder_height(node):
            if not node:
                return 0
            left_height = preorder_height(node.left)
            right_height = preorder_height(node.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
                return
            return max(left_height, right_height) + 1

        preorder_height(root)
        return self.balanced


if __name__ == "__main__":
    case1_input = TreeNode(3, TreeNode(
        9), TreeNode(20, TreeNode(15), TreeNode(7)))
    case1_output = True
    case2_input = TreeNode(1, TreeNode(
        2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    case2_output = False
    case3_input = TreeNode(None)
    case3_output = True
    case4_input = TreeNode(1,
                           TreeNode(2, TreeNode(3, TreeNode(4), None), None),
                           TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    case4_output = False
    class_function = Solution()
    for function in [class_function.is_balanced_recursive]:
        assert function(case1_input) == case1_output
        assert function(case2_input) == case2_output
        assert function(case3_input) == case3_output
        assert function(case4_input) == case4_output
