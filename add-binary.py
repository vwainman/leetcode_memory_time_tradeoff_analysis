# https://leetcode.com/problems/add-binary/description/
# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a: str, b: str) -> str:
    # Time: O(Max(n, m))
    # Memory: sum O(~Max(n, m)), carry O(1)
    sum: str = ""
    carry: int = 0

    while a or b or carry:
        if a:
            carry += int(a[-1])
            a = a[:-1]
        if b:
            carry += int(b[-1])
            b = b[:-1]
        sum = str(carry % 2) + sum
        carry = carry // 2

    return sum


if __name__ == "__main__":
    assert addBinary("11", "1") == "100"
    assert addBinary("1010", "1011") == "10101"
