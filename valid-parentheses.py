# https://leetcode.com/problems/valid-parentheses/description/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.

class ValidParenthesesSolution:
    open_brackets: list[chr] = ["{", "(", "["]
    closed_brackets: list[chr] = ["}", ")", "]"]
    open_closed_brackets: dict[chr] = {open_: closed for (open_, closed)
                                       in zip(open_brackets, closed_brackets)}

    def __init__(self, s: str):
        self.s = s
        self.stack: list[chr] = []

    def is_invalid_closed_bracket(self, next_closed_bracket: chr):
        if not self.stack:
            return True
        expected_closed: chr = self.open_closed_brackets[self.stack.pop()]
        if expected_closed != next_closed_bracket:
            return True
        return False

    def is_valid_by_stack(self) -> bool:
        # Time: O(n)
        # Memory: O(n)
        for char in self.s:
            if char in self.open_brackets:
                self.stack.append(char)
            elif self.is_invalid_closed_bracket(char):
                return False
        return len(self.stack) == 0


if __name__ == "__main__":
    case_inputs = ["()", "()[]{}", "(]"]
    case_outputs = [True, True, False]
    for i, input in enumerate(case_inputs):
        sol = ValidParenthesesSolution(input)
        assert sol.is_valid_by_stack() == case_outputs[i]
