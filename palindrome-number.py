"""
Given an integer x, return true if x is palindrome integer.

Constraints:
-2^31 <= x <= (2^31) - 1

"""


class PalindromeNumberSolution:
    x: int

    def __init__(self, x: int) -> None:
        self.x = x

    def is_palindrome(self) -> bool:
        # Time: O(1)
        # Memory: O(1)
        str_x = str(self.x)
        half_len = len(str_x) // 2
        start_half = str_x[:half_len]
        if is_odd(half_len):
            half_len += 1
        end_half = str_x[half_len:]
        return start_half == end_half


def is_odd(num: int) -> bool:
    return num % 2 == 0


if __name__ == "__main__":
    """ Further optimization is negligible in performance eval
        and memory/timing tests are unnecessary. """
    print(PalindromeNumberSolution(121).is_palindrome())
    print(PalindromeNumberSolution(-121).is_palindrome())
    print(PalindromeNumberSolution(10).is_palindrome())
