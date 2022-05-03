# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of
# strings.

from dataclasses import dataclass


@dataclass
class LongestCommonPrefixSolution:
    strs: list[str]

    def longest_common_prefix(self) -> str:
        # Time: O(n)
        # Memory: O(1)
        # if there's only one string, return it
        if len(self.strs) == 1:
            return self.strs[0]

        prefix = ""
        i = 0
        longest_common_reached = False
        reference_str = self.strs[0]

        while not longest_common_reached:
            if i <= len(reference_str):
                substring_ref = reference_str[:i]
            else:
                break
            for str_ in self.strs[1:]:
                if (i < len(str_) and str_[:i] != substring_ref) or (len(str_) < i):
                    longest_common_reached = True
                    break
            else:
                prefix = substring_ref
                i += 1
        return prefix


if __name__ == '__main__':
    case1_input = ["flower", "flow", "flight"]
    case1_output = "fl"
    case2_input = ["dog", "racecar", "car"]
    case2_output = ""
    case3_input = ["flower", "flower", "flower", "flower"]
    case3_output = "flower"
    case4_input = ["ab", "a"]
    case4_output = "a"
    assert LongestCommonPrefixSolution(
        case1_input).longest_common_prefix() == case1_output
    assert LongestCommonPrefixSolution(
        case2_input).longest_common_prefix() == case2_output
    assert LongestCommonPrefixSolution(
        case3_input).longest_common_prefix() == case3_output
    assert LongestCommonPrefixSolution(
        case4_input).longest_common_prefix() == case4_output
