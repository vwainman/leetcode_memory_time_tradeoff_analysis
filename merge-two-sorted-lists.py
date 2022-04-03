# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        # empty linked list
        if self.val is None and self.next is None:
            return 0

        i: int = 1
        node = self.next
        while node is not None:
            i += 1
            node = node.next
        return i

    def __str__(self):
        string = str(self.val) + "->"
        node = self.next
        while node is not None:
            string = string + str(node.val) + "->"
            node = node.next
        return string[:-2]

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.__str__() == other.__str__()


class MergeTwoListsSolution:

    def __init__(self, list1, list2):
        self.l1 = list1
        self.l2 = list2
        self.merged = ListNode()
        self.merged_head = self.merged
        self.l1_tail_reached = False
        self.l2_tail_reached = False

    def merge_and_hop_node(self) -> None:
        if self.l1.val < self.l2.val:
            self.merged.val = self.l1.val
            if len(self.l1) > 1:
                self.l1 = self.l1.next
            else:
                self.l1_tail_reached = True
        else:
            self.merged.val = self.l2.val
            if len(self.l2) > 1:
                self.l2 = self.l2.next
            else:
                self.l2_tail_reached = True

    def merge_two_lists(self) -> Optional[ListNode]:
        if self.l1.val is None and self.l2.val is None:
            return ListNode(val=None, next=None)
        elif self.l1.val is None:
            return self.l2
        elif self.l2.val is None:
            return self.l1

        while not self.l1_tail_reached and not self.l2_tail_reached:
            # sub in the correct node
            self.merge_and_hop_node()
            # setup next node
            self.merged.next = ListNode()
            self.merged = self.merged.next

        # merge leftover
        if self.l2_tail_reached:
            self.merged.val = self.l1.val
            self.merged.next = self.l1.next
        elif self.l1_tail_reached:
            self.merged.val = self.l2.val
            self.merged.next = self.l2.next
        else:
            self.merged = None

        return self.merged_head


def link_list(values: List[int]) -> ListNode:
    if len(values) == 0:
        return ListNode(None, None)

    head = ListNode()
    node = head
    for value in values[:-1]:
        node.val = value
        node.next = ListNode()
        node = node.next
    node.val = values[-1]
    node.next = None
    return head


if __name__ == "__main__":
    ex_list1 = link_list([1, 2, 4])
    ex_list2 = link_list([1, 3, 4])
    case1_input = MergeTwoListsSolution(ex_list1, ex_list2)
    case1_output = link_list([1, 1, 2, 3, 4, 4])
    assert case1_input.merge_two_lists() == case1_output
    case2_input = MergeTwoListsSolution(link_list([]), link_list([]))
    case2_output = link_list([])
    assert case2_input.merge_two_lists() == case2_output
    case3_input = MergeTwoListsSolution(link_list([]), link_list([0]))
    case3_output = link_list([0])
    assert case3_input.merge_two_lists() == case3_output
