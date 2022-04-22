# https://leetcode.com/problems/container-with-most-water/description/
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


from typing import List


def get_max_line_area(start_line: int, height: List[int], left_i: int) -> int:
    """ get the maximum volume for the line at line[i]
        by reverse traversal, outputting the best possible max
    """
    max_so_far = 0
    right_i = len(height) - 1
    while right_i != left_i:
        max_possible = start_line * (right_i - left_i)
        if max_possible <= max_so_far:
            break
        current_volume = min(start_line, height[j]) * (right_i - left_i)
        max_so_far = max(max_so_far, current_volume)
        if max_so_far == max_possible:
            break
        right_i -= 1
    return max_so_far


def max_area_single_pointer(height: List[int]) -> int:
    # Time: O(!n^2) - caused LeetCode timeout
    # Memory: O(1)
    """Traverse from the beginning to the end to check every possible
       combination of volumes
    """
    maximum: int = 0
    for left_i, start_line in enumerate(height):
        line_max = get_max_line_area(start_line, height, left_i)
        maximum = max(line_max, maximum)
    return maximum


def max_area_two_pointers(heights: List[int]) -> int:
    # Time: O(n)
    # Memory: O(1)
    """Traverse from the left and right with each pointer
       moving in the opposite direction conditioned on the smaller
       line height.
    """

    left_i: int = 0
    right_i: int = len(heights) - 1
    max_vol: int = 0

    while left_i != right_i:
        width = right_i - left_i
        height = min(heights[left_i], heights[right_i])
        max_vol = max(max_vol, height * width)
        if heights[left_i] < heights[right_i]:
            left_i += 1
        else:
            right_i -= 1

    return max_vol
