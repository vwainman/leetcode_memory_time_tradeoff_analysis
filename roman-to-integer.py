""" Roman to Integer

https://leetcode.com/problems/roman-to-integer/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D
and M.


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27 is
written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is
written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There
are six instances where subtraction is used:


I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.


Given a roman numeral, convert it to an integer.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999]. """


class RomanToIntSolution:
    s: str
    roman_vals: dict

    def __init__(self, s: str):
        self.s = s
        self.roman_val: dict = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
        }
        self.dbl_roman_val: dict = {
            "IV": 4, "IX": 9, "XL": 40,
            "XC": 90, "CD": 400, "CM": 900
        }

    def each_roman_to_int(self) -> int:
        # convert every roman or double roman val
        val = 0
        i = 0
        while i != len(self.s):
            if len(self.s[i:]) >= 2 and self.s[i:i+2] in self.dbl_roman_val:
                val += self.dbl_roman_val[self.s[i:i+2]]
                i += 2
            else:
                val += self.roman_val[self.s[i]]
                i += 1
        return val


if __name__ == "__main__":
    case1_input: str = "III"
    case1_output: int = 3  # III=3
    assert RomanToIntSolution(
        case1_input).each_roman_to_int() == case1_output
    case2_input: str = "LVIII"
    case2_output: int = 58  # L=50, V=5, III=3
    assert RomanToIntSolution(
        case2_input).each_roman_to_int() == case2_output
    case3_input: str = "MCMXCIV"
    case3_output: int = 1994  # M=1000, CM=900, XC=90, IV=4
    assert RomanToIntSolution(
        case3_input).each_roman_to_int() == case3_output
