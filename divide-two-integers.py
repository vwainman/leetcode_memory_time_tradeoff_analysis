# https://leetcode.com/problems/divide-two-integers/description/
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31
# - 1, and if the quotient is strictly less than -2^31, then return -2^31.
#
# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0


MAX_QUOTIENT = (2 ** 31) - 1
MIN_QUOTIENT = -(MAX_QUOTIENT + 1)


def divide_naive(dividend: int, divisor: int) -> int:
    # Works but is unbearably inefficient for large dividends and small divisors
    # Time: O(n)
    # Space: O(1)
    sign = -1 if (dividend < 0) is (divisor > 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        if dividend >= 0:
            quotient += 1
    quotient *= sign
    if quotient > MAX_QUOTIENT:
        return MAX_QUOTIENT
    elif quotient < MIN_QUOTIENT:
        return MIN_QUOTIENT
    else:
        return quotient


def divide_bitwise_manipulation(dividend: int, divisor: int) -> int:
    # Time: O(log(n))
    # Space: O(1)
    sign = -1 if (dividend < 0) is (divisor > 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        temp, n_divided = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += n_divided
            n_divided <<= 1
            temp <<= 1
    quotient *= sign
    if quotient > MAX_QUOTIENT:
        return MAX_QUOTIENT
    elif quotient < MIN_QUOTIENT:
        return MIN_QUOTIENT
    else:
        return quotient


if __name__ == "__main__":
    case1_inputs = (10, 3)
    case1_output = 3
    case2_inputs = (7, -3)
    case2_output = -2
    for function in [divide_naive, divide_bitwise_manipulation]:
        assert function(*case1_inputs) == case1_output
        assert function(*case2_inputs) == case2_output
