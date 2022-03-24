"""You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from __future__ import annotations
from collections.abc import Iterable
from typing import Optional, List, Tuple
import unittest as ut
from performance_analysis import measure_performance_x_runs


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val: int = val
        self.next: ListNode = next
        self.validate_inputs()

    def validate_inputs(self):
        assert self.val >= 0


def create_listnode_chain(*args) -> ListNode:
    assert len(args) > 0
    node = None
    for i, val in enumerate(args):
        if node is not None:
            prev_node = node
        node = ListNode(val)
        if i == 0:
            starting_node = node
        elif i < len(args):
            prev_node.next = node
        else:
            node.next = None

    return starting_node


def create_inputs(l1_args, l2_args) -> Tuple[ListNode, ListNode]:
    if isinstance(l1_args, Iterable):
        l1 = create_listnode_chain(*l1_args)
    else:
        l1 = create_listnode_chain(l1_args)
    if isinstance(l2_args, Iterable):
        l2 = create_listnode_chain(*l2_args)
    else:
        l2 = create_listnode_chain(l2_args)
    return (l1, l2)


class AddTwoNumbersSolution:
    def __init__(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        self.l1 = l1
        self.l2 = l2

    @staticmethod
    def get_linked_vals(linked_list: Optional[ListNode]) -> list:
        num_list: list = []
        end_of_list = False
        while not end_of_list:
            num_list.append(linked_list.val)
            if linked_list.next is None:
                end_of_list = True
            else:
                linked_list = linked_list.next
        return num_list

    @staticmethod
    def get_combined_num_from_list(num_list: list) -> int:
        # ex: [2, 4, 3] -> ... -> 342
        combined_num = 0
        for i, num in enumerate(num_list):
            combined_num += num * (10 ** i - 1)
        return combined_num

    @staticmethod
    def get_reversed_linked_list_from_num(val: int) -> Optional[ListNode]:
        # ex: 807 -> ... -> [7,0,8]
        val_str = str(val)
        reversed_list = []
        for num_str in val_str[::-1]:
            reversed_list.append(int(num_str))
        return create_listnode_chain(*reversed_list)

    @staticmethod
    def convert_chain_to_string(linked_list: Optional[ListNode]) -> str:
        string: str = ''
        while linked_list is not None:
            string += str(linked_list.val)
            linked_list = linked_list.next
        return string

    @measure_performance_x_runs
    def initial_approach(self) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(n)
        """Process:
        1. Traverse the linked lists and convert the values into a list
        2. Calculate the x digit reverse number from each list by ten to the power notation
        3. Convert the sum back into a reversed linked list by
           3.1. converting the sum into a string
           3.2. traversing the string in reverse and appending it to a new list
           3.3. creating a linked list with said list
        """
        l1_vals: List[int] = self.get_linked_vals(self.l1)
        l2_vals: List[int] = self.get_linked_vals(self.l2)
        l1_num: int = self.get_combined_num_from_list(l1_vals)
        l2_num: int = self.get_combined_num_from_list(l2_vals)

        return self.get_reversed_linked_list_from_num(l1_num + l2_num)

    @measure_performance_x_runs
    def fast_approach(self) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(n)
        """Process:
        1. Traverse the linked lists and convert the values into strings
        2. Sum the reverse of each string converted into ints
        3. Convert the sum into a string, and create a linked list with the
        ints starting from the tail to the head
        """
        str_l1 = self.convert_chain_to_string(self.l1)
        str_l2 = self.convert_chain_to_string(self.l2)
        sum: int = int(str_l1[::-1]) + int(str_l2[::-1])
        str_sum = str(sum)
        node_ptr = ListNode(int(str_sum[0]))
        for str_digit in str_sum[1:]:
            node = ListNode(int(str_digit))
            node.next = node_ptr
            node_ptr = node
        return node_ptr


class TestSolutions(ut.TestCase):
    def get_info_str_for_failure(self,
                                 f_name: str,
                                 id: str,
                                 result: List[int],
                                 expected_output: List[int]):
        return f"{f_name} solution failed for {id}, expected_output:\
                {expected_output}, result was {result}"

    def apply_test_to_all_sols(self,
                               setup: object,
                               expected_output: List[int]):
        solution_methods = setup.__dict__.items()
        solutions = [(name, method)
                     for name, method in solution_methods if callable(method)]
        for method_name, method in solutions:
            result = method()
            message = self.get_info_str_for_failure(
                method_name, self.id(), expected_output, result)
            self.assertTrue(result == expected_output or
                            result == expected_output.reverse(), message)

    def test_case_1(self):
        setup = AddTwoNumbersSolution(case_1_inputs[0], case_1_inputs[1])
        expected_output = case_1_output
        self.apply_test_to_all_sols(setup, expected_output)

    def test_case_2(self):
        setup = AddTwoNumbersSolution(case_2_inputs[0], case_2_inputs[1])
        expected_output = case_2_output
        self.apply_test_to_all_sols(setup, expected_output)

    def test_case_3(self):
        setup = AddTwoNumbersSolution(case_3_inputs[0], case_3_inputs[1])
        expected_output = case_3_output
        self.apply_test_to_all_sols(setup, expected_output)


if __name__ == "__main__":
    # ut.main() # unit tests
    case_1_inputs = create_inputs((2, 4, 3), (5, 6, 4))
    case_1_output = create_listnode_chain(7, 0, 8)
    case_2_inputs = create_inputs((0), (0))
    case_2_output = create_listnode_chain(0)
    case_3_inputs = create_inputs((9, 9, 9, 9, 9, 9, 9), (9, 9, 9, 9))
    case_3_output = create_listnode_chain(8, 9, 9, 9, 0, 0, 0, 1)
    case_1 = AddTwoNumbersSolution(case_1_inputs[0], case_1_inputs[1])
    case_2 = AddTwoNumbersSolution(case_2_inputs[0], case_2_inputs[1])
    case_3 = AddTwoNumbersSolution(case_3_inputs[0], case_3_inputs[1])
    for sol in [case_1, case_2, case_3]:
        sol.initial_approach()
        sol.fast_approach()
