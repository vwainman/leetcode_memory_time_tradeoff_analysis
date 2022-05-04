# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    node_values = []
    node_stack = []
    current_node = root
    while True:
        # traverse current node's all the way left
        # while appending its prev nodes to a stack
        while current_node:
            node_stack.append(current_node)
            current_node = current_node.left
        # we'll know we're done traveling once the stack is empty
        if not node_stack:
            break
        # otherwise, apply LIFO to meet inorder requirements
        current_node = node_stack.pop()
        # left is no longer viable, append to visited values
        node_values.append(current_node.val)
        # now attempt traversal of the previous node (now current) to the right
        current_node = current_node.right
    return node_values


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    node_values = []

    def recursive_helper(node: Optional[TreeNode], visited_vals: List[int]) -> List[int]:
        if node:
            recursive_helper(node.left, visited_vals)
            visited_vals.append(node.val)
            recursive_helper(node.right, visited_vals)

    recursive_helper(root, node_values)
    return node_values


if __name__ == "__main__":
    case1_input = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    case1_output = [1, 3, 2]
    for function in [inorder_traversal_recursive, inorder_traversal_iterative]:
        assert function(case1_input) == case1_output
