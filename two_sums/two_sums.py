"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution,
and you may not use the same element twice.
- You can return the answer in any order.
Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""

from functools import wraps
from memory_profiler import memory_usage
from time import time
from typing import List, TypeVar, Tuple, Callable
import unittest as ut

QUARTER_SECOND = 0.25
HALF_SECOND = 0.5
ONE_SECOND = 1
MAX_LENGTH = 10 ** 4
MIN_LENGTH = 2
MAX_INT = 10 ** 9
MIN_INT = -MAX_INT
LENGTH_CONSTRAINT_STR = "list length constraint unmet"
TARGET_CONSTRAINT_STR = "target numeric constraint unmet"
ELEMENT_CONSTRAINT_STR = "element numeric constraint unmet"
return_type = TypeVar("return_type")
max_len_input = ([0 for _ in range(MAX_LENGTH - 2)] + [1, 2], 3)
min_len_input = ([1, 1], 2)
case_1_input = ([2, 7, 11, 15], 9)
case_2_input = ([3, 2, 4], 6)
case_3_input = ([3, 2, 4], 6)


def time_algorithm(f: Callable,
                   n_runs: int,
                   *args,
                   **kw) -> Tuple[return_type, float]:
    time_start: float = time()
    for _ in range(n_runs):
        result: Tuple[return_type, float] = f(*args, **kw)
    time_end: float = time()
    total_time = time_end - time_start
    return (result, total_time)


def determine_n_runs(time: float) -> int:
    if time <= QUARTER_SECOND:
        return 1000
    elif time <= HALF_SECOND:
        return 100
    else:
        return 1


def measure_performance_x_runs(f):
    """Performance decorator to measure the time required to run
    the function x times with identical inputs, and the memory
    required for a single run."""
    @wraps(f)
    def wrap(*args, **kw):
        # measure one run's max memory intake
        mem = memory_usage(proc=(f, args, kw), max_usage=True)
        # measure the time on a single run to determine the n of iterations
        result, time = time_algorithm(f, 1, *args, **kw)
        n_runs = determine_n_runs(time)
        # apply iterations to better compare negligible runtime differences
        _, time = time_algorithm(f, n_runs, *args, **kw)
        if len(args[0].nums) > 10:
            print(
                f"{f.__name__} with nums = long list and"
                f" target = {args[0].target} stats:")
        else:
            print(f"{f.__name__} with nums = {args[0].nums}"
                  f" and target = {args[0].target} stats:")
        print(f"Total time for {n_runs} run(s): {time}")
        print(f"Total memory for one run: {mem}\n")
        return result
    return wrap


class TwoSumSolutions:
    def __init__(self, nums: List[int], target: int):
        self.nums = nums
        self.target = target
        self.validate_inputs()

    def validate_inputs(self):
        assert MIN_LENGTH <= len(self.nums) <= MAX_LENGTH,\
            LENGTH_CONSTRAINT_STR
        assert MIN_INT <= self.target <= MAX_INT, TARGET_CONSTRAINT_STR
        for element in self.nums:
            assert isinstance(element, int) and\
                MIN_INT <= element <= MAX_INT, ELEMENT_CONSTRAINT_STR

    @measure_performance_x_runs
    def two_sum_brute_force(self) -> List[int]:
        # O(n^2) solution
        for i, num1 in enumerate(self.nums):
            for j, num2 in enumerate(self.nums[i+1:]):
                if num1 + num2 == self.target:
                    return [i, j]

    @measure_performance_x_runs
    def two_sum_mapped_nums(self) -> List[int]:
        # O(n) solution
        """Mapping the difference between the target and numbers
           encountered provides us with the information necessary
           to know which valid number(s) to look for next"""
        differences_index_map: dict = {}
        for i, num in enumerate(self.nums):
            if num in differences_index_map:
                return [differences_index_map[num], i]
            else:
                differences_index_map[self.target - num] = i


class TestSolutions(ut.TestCase):
    def get_info_str_for_failure(self,
                                 f_name: str,
                                 id: str,
                                 result: List[int],
                                 expected_output: List[int]):
        return f"{f_name} solution failed for {id}, expected_output:\
                 {expected_output}, result was {result}"

    def apply_test_to_all_sols(self,
                               setup: TwoSumSolutions,
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

    def test_max_length_constraint(self):
        nums, target = max_len_input
        setup = TwoSumSolutions(nums, target)
        expected_output = [len(nums) - 1, len(nums) - 2]
        self.apply_test_to_all_sols(setup, expected_output)

    def test_min_length_constraint(self):
        nums, target = min_len_input
        setup = TwoSumSolutions(nums, target)
        expected_output = [0, 1]
        self.apply_test_to_all_sols(setup, expected_output)

    def test_case_1(self):
        nums, target = case_1_input
        setup = TwoSumSolutions(nums, target)
        expected_output = [0, 1]
        self.apply_test_to_all_sols(setup, expected_output)

    def test_case_2(self):
        nums, target = case_2_input
        setup = TwoSumSolutions(nums, target)
        expected_output = [1, 2]
        self.apply_test_to_all_sols(setup, expected_output)

    def test_case_3(self):
        nums, target = case_3_input
        setup = TwoSumSolutions(nums, target)
        expected_output = [0, 1]
        self.apply_test_to_all_sols(setup, expected_output)


if __name__ == "__main__":
    # assertion tests with ut.main()
    # performance evals
    max_len_case = TwoSumSolutions(*max_len_input)
    min_len_case = TwoSumSolutions(*min_len_input)
    case_1 = TwoSumSolutions(*case_1_input)
    case_2 = TwoSumSolutions(*case_2_input)
    case_3 = TwoSumSolutions(*case_3_input)
    for sol in [max_len_case, min_len_case, case_1, case_2, case_3]:
        sol.two_sum_brute_force()
        sol.two_sum_mapped_nums()
