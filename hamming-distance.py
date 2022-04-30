# https://leetcode.com/problems/hamming-distance/description/
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.

def hamming_distance(x: int, y: int) -> int:
    # Time: O(max(n, m)) where n = len(x), m = len(y)
    # Memory: O(n + m)
    x: str = str(bin(x))[2:]
    y: str = str(bin(y))[2:]
    len_diff: int = len(x) - len(y)
    diff_count: int = 0
    if len_diff < 0:
        x = ("0" * abs(len_diff)) + x
    elif len_diff > 0:
        y = ("0" * len_diff) + y
    for x_bit, y_bit in zip(x, y):
        if x_bit != y_bit:
            diff_count += 1
    return diff_count


if __name__ == "__main__":
    case1_input = (1, 4)
    case1_output = 2
    case2_input = (3, 1)
    case2_output = 1
    assert hamming_distance(*case1_input) == case1_output
    assert hamming_distance(*case2_input) == case2_output
