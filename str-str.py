# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
# Constraints: 1 <= len(haystack) <= len(needle) <= 10^4


class StrStrSolution:

    def __init__(self, haystack: str, needle: str):
        if len(haystack) < len(needle):
            raise ValueError("Haystack should be larger than needle")
        self.haystack: str = haystack
        self.needle: str = needle

    def str_str(self) -> int:
        if len(self.needle) == 0:
            return 0
        needle_len = len(self.needle)
        haystack_len = len(self.haystack)
        i: int = 0
        while i + needle_len <= haystack_len:
            if self.haystack[i:i+needle_len] == self.needle:
                return i
            i += 1
        return -1


if __name__ == "__main__":
    case1_input = StrStrSolution("hello", "ll")
    case2_input = StrStrSolution("aaaaa", "bba")
    case3_input = StrStrSolution("a", "")
    case4_input = StrStrSolution("abcdefg", "g")
    assert case1_input.str_str() == 2
    assert case2_input.str_str() == -1
    assert case3_input.str_str() == 0
    assert case4_input.str_str() == 6
