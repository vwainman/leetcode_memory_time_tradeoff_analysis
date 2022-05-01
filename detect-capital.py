# https://leetcode.com/problems/detect-capital/description/
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
# Given a string word, return true if the usage of capitals in it is right.

def detect_capital_use_performant(word: str) -> bool:
    # Time: O(n)
    # Space: O(1)
    # true: all lower case or first letter uppercase or all uppercase
    # assume innocent until proven guilty
    # hardly readable, needs to be refactored
    all_lower = True
    all_upper = True
    first_upper_only = True
    if word[0].islower():
        all_upper = False
        first_upper_only = False
    for char in word[1:]:
        if char.isupper():
            first_upper_only = False
            all_lower = False
        elif char.islower():
            all_upper = False
    return all_lower or all_upper or first_upper_only


def detect_capital_use_simple(word: str) -> bool:
    # Time: O(2n)
    # Space: O(1)
    return len(word) == 1 or word[1:].islower() or word.isupper()
