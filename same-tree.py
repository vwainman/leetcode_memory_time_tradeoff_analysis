# https://leetcode.com/problems/same-tree/description/
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # recursively travel down each tree, checking that each node and subsequent
    # path are equivalent.
    # Time = O(n) or O(m), whichever is shortest
    # Memory = O(1)

    # recurse down the tree until both nodes are no longer TreeNodes
    if isinstance(p, TreeNode) and isinstance(q, TreeNode):
        return p.val == q.val \
            and isSameTree(p.left, q.left) \
            and isSameTree(p.right, q.right)
    # should one of the roots be a tree node, check if it has roots
    # if it doesn't, replace that node with its inherent value
    elif isinstance(p, TreeNode) and p.left is None and p.right is None:
        p = p.val
    elif isinstance(q, TreeNode) and q.left is None and p.right is None:
        q = q.val
    return p == q


if __name__ == "__main__":
    case1_inputs = {"p": TreeNode(1, 2, TreeNode(3)), "q": TreeNode(1, 2, 3)}
    case2_inputs = {"p": TreeNode(1, 2, None),    "q": TreeNode(1, None, 2)}
    case3_inputs = {"p": TreeNode(1, 2, 1), "q": TreeNode(1, 1, 2)}
    case1_output = True
    case2_output = False
    case3_output = False
    assert isSameTree(case1_inputs["p"], case1_inputs["q"]) == case1_output
    assert isSameTree(case2_inputs["p"], case2_inputs["q"]) == case2_output
    assert isSameTree(case3_inputs["p"], case3_inputs["q"]) == case3_output
