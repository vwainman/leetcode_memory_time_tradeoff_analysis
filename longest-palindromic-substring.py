# https://leetcode.com/problems/longest-palindromic-substring/description/

from collections import Dict


class LongestPalindromeSolution:
    s: str
    char_counter: Dict[int]
    pair_count: int
    odd_count: int

    def __init__(self, s: str) -> None:
        self.s = s
        self.char_counts = {}
        self.odd_count = 0

    def save_char_frequencies(self):
        for char in self.s:
            if char not in self.char_counts:
                self.char_counts[char] = 0
            else:
                self.char_counts[char] += 1

    def count_odds(self):
        for _, freq in self.char_counts.items():
            if freq % 2 != 0:
                self.odd_count += 1

    def longestPalindrome(self) -> int:
        self.save_char_frequencies()
        self.count_odds()
        if self.odd_count != 0:
            # exclude middle char from consideration
            return len(self.s) - (self.odd_count + 1)
        else:
            return len(self.s)
