"""Given a string s, find the length of the longest
substring without repeating characters."""


class Solution:

    def __init__(self, s: str):
        self.s: int = s

    def length_of_longest_non_repeating_substring(self) -> int:
        start_i: int = 0
        max_len: int = 0
        used_chars_i: dict = {}
        for i, char in enumerate(self.s):
            if char in used_chars_i and start_i <= used_chars_i[char]:
                start_i = used_chars_i[char] + 1
            else:
                max_len = max(max_len, i - start_i + 1)
            used_chars_i[char] = i
        return max_len


if __name__ == "__main__":
    case1_input: str = "abcabcbb"
    case1_output: int = 3
    assert Solution(
        case1_input).length_of_longest_non_repeating_substring() == 3
    case2_input: str = "bbbbb"
    case2_output: int = 1
    assert Solution(
        case2_input).length_of_longest_non_repeating_substring() == 1
    case3_input: str = "pwwkew"
    case3_output: int = 3
    assert Solution(
        case3_input).length_of_longest_non_repeating_substring() == 3
