# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        while True:
            if not self and not other:
                break
            elif (not self and other) or (self and not other):
                return False
            if self.val == other.val:
                self = self.next
                other = other.next
            else:
                return False
        return True


def remove_Nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Time: O(n)
    # Space: O(n)
    node_list = []
    node = head
    while node:
        node_list.append(node)
        node = node.next
    if len(node_list) == 1:
        return None
    elif n == 1:
        node_list[-2].next = None
    elif n == len(node_list):
        head = node_list[1]
    else:
        node_list[-n - 1].next = node_list[-n + 1]
    return head


if __name__ == "__main__":
    case1_inputs = (ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    case1_output = ListNode(1, ListNode(
        2, ListNode(3, ListNode(5))))
    case2_inputs = (ListNode(1), 1)
    case2_output = None
    case3_inputs = (ListNode(1, ListNode(2)), 1)
    case3_output = ListNode(1)
    assert remove_Nth_from_end(*case1_inputs) == case1_output
    assert remove_Nth_from_end(*case2_inputs) == case2_output
    assert remove_Nth_from_end(*case3_inputs) == case3_output
