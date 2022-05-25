# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

def remove_duplicates(s: str) -> str:
    # Time: O(n)
    # Space: O(n)
    stack = []
    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
