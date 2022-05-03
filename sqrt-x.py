# https://leetcode.com/problems/sqrtx/description/
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.


def my_sqrt_naive(x: int) -> int:
    # Time: O(n)
    # Space: O(1)
    root = 0
    while root*root < x:
        root += 1
    if (root*root > x):
        # floating point answer, truncate to last root
        return root - 1
    return root


def my_sqrt_bin_search(x: int) -> int:
    # Time: O(log(n))
    # Space: O(1)
    low = 0 if x != 1 else 1
    high = x
    last_mid = -1

    while True:
        mid = (low + high)//2
        if (mid * mid == x or last_mid == mid):
            break
        elif (mid * mid > x):
            high = mid
        else:
            low = mid
        last_mid = mid
    return mid


if __name__ == "__main__":
    for function in [my_sqrt_naive, my_sqrt_bin_search]:
        assert function(4) == 2
        assert function(8) == 2
