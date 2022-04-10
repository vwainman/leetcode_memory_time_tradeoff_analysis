# https://leetcode.com/problems/plus-one/description/
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of
# digits.

from dataclasses import dataclass
from typing import List


@dataclass
class PlusOneSolution:
    digits: List[int]

    def plus_one(self) -> List[int]:
        # Time: O(n)
        # Memory: O(1)
        # badly written, but the logic is based on the elementary math approach
        carry_over = False
        if self.digits[-1] == 9:
            carry_over = True
            self.digits[-1] = 0
        else:
            self.digits[-1] += 1
        if carry_over:
            n_digits = len(self.digits)
            for i in range(n_digits - 2, -1, -1):
                if self.digits[i] == 9:
                    self.digits[i] = 0
                else:
                    self.digits[i] += 1
                    break
            else:
                self.digits.insert(0, 1)

        return self.digits

    def cleaner_plus_one(self) -> List[int]:
        # Time: O(n), albeit more efficient
        # Memory: O(1), utilizing 4 bytes to keep tabs on i alone
        # a lot cleaner and straightforward
        i = len(self.digits) - 1
        while self.digits[i] == 9:
            self.digits[i] = 0
            i -= 1
        if i >= 0:
            self.digits[i] += 1
        else:
            self.digits.insert(0, 1)

        return self.digits


if __name__ == "__main__":
    test = PlusOneSolution([0])
    test.plus_one()
    print(test.digits)
