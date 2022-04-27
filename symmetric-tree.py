# https://leetcode.com/problems/symmetric-tree/description/
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric_recursive(root: Optional[TreeNode]) -> bool:
    # Time: O(n_child_nodes / 2)
    # Memory: O(1)

    if root is None:
        return True

    def is_mirrored(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return True

        if left.val == right.val:
            outside_child_nodes = is_mirrored(left.left, right.right)
            inside_child_nodes = is_mirrored(left.right, right.left)
            return outside_child_nodes and inside_child_nodes
        else:
            return False

    return is_mirrored(root.left, root.right)


def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
    # Top to bottom
    # Time: equivalent
    # Memory: O(n_nodes)

    if root is None:
        return True

    tree_stack = [[root.left, root.right]]

    while len(tree_stack) != 0:
        left, right = tree_stack.pop(0)
        if left is None and right is None:
            continue
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            tree_stack.insert(0, [left.left, right.right])
            tree_stack.insert(0, [left.right, right.left])
        else:
            # left.val != right.val
            return False
    return True


if __name__ == "__main__":
    case1_input = TreeNode(1,
                           TreeNode(2, TreeNode(3), TreeNode(4)),
                           TreeNode(2, TreeNode(4), TreeNode(3)))
    case2_input = TreeNode(1,
                           TreeNode(2, None, TreeNode(3)),
                           TreeNode(2, None, TreeNode(3)))
    case1_output = True
    case2_output = False

    assert is_symmetric_recursive(case1_input) == case1_output
    assert is_symmetric_iterative(case2_input) == case2_output
