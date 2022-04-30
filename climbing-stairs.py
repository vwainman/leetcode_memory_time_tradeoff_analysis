# https://leetcode.com/problems/climbing-stairs/description/
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?


from copy import copy


def climb_stairs_top_down(n: int) -> int:
    # Starting from the top, with each step reached by 1 or 2 possiblities
    # Time: O(2^n)
    # Memory: O(1)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stairs_top_down(n - 1) + climb_stairs_top_down(n - 2)


class Solution:
    def __init__(self):
        self.hash_map = {1: 1, 2: 2}

    def climb_stairs_top_down_memoization(self, n: int) -> int:
        # Same logic as above, except memory is used to eliminate repeated
        # executions
        # Time: O(n^2?)
        # Memory: O(n)
        if n not in self.hash_map:
            self.hash_map[n] = self.climb_stairs_top_down_memoization(n - 1) \
                + self.climb_stairs_top_down_memoization(n - 2)
        return self.hash_map[n]


def climb_stairs_bottom_up(n: int) -> int:
    # Each n_way can be calculated by summing the previous two steps n_way
    # Time: O(n)
    # Memory: O(1)
    if n == 1:
        return 1
    last_two_n_ways: list = [1, 2]
    for _ in range(n - 2):
        temp = copy(last_two_n_ways[-1])
        last_two_n_ways[-1] += last_two_n_ways[0]
        last_two_n_ways[0] = temp

    return last_two_n_ways[-1]


if __name__ == "__main__":
    case_input_output = {2: 2, 3: 3, 4: 5, 5: 8, 6: 13}
    for key, value in case_input_output.items():
        assert climb_stairs_top_down(key) == value
        assert Solution().climb_stairs_top_down_memoization(key) == value
        assert climb_stairs_bottom_up(key) == value
