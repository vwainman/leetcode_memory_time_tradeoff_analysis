# https://leetcode.com/problems/assign-cookies/description/
#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie
# that the child will be content with; and each cookie j has a size s[j]. If
# s[j] >= g[i], we can assign the cookie j to the child i, and the child i will
# be content. Your goal is to maximize the number of your content children and
# output the maximum number.

from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    # Time: O(nlog(n) + mlog(m))
    # Space: O(1)

    g.sort()
    s.sort()
    max_content = 0

    i, j = 0, 0
    while i != len(s) and j != len(g):
        # pass on cookie sizes until one meets the current greed factor
        if s[i] >= g[j]:
            max_content += 1
            j += 1
        i += 1

    return max_content
