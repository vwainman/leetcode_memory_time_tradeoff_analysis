# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

def length_of_last_word(s: str) -> int:
    # Time = O(n + m) where n = length of last word and m = length of trailing spaces
    # Memory = O(1)
    # Traverse the string in reverse to count
    # the length of the last word

    # remove trailing spaces
    s_rstripped = s.rstrip(' ')
    i: int = -1
    length: int = 0

    # travel by reverse indexing
    while -i < len(s_rstripped):
        if s_rstripped[i] == " ":
            break

        i -= 1
        length += 1

    return length


if __name__ == "__main__":
    case_inputs = ["Hello World",
                   "   fly me   to   the moon  ",
                   "luffy is still joyboy"]
    case_outputs = [5, 4, 6]
    for i in range(len(case_inputs)):
        assert length_of_last_word(case_inputs[i]) == case_outputs[i]
