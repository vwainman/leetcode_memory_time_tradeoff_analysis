# https://leetcode.com/problems/goat-latin/description/
#
# You are given a string sentence that consist of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.) The rules of Goat Latin are as follows:
#
# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to
# the end of the word.
#
# For example, the word "apple" becomes "applema".
#
# If a word begins with a consonant (i.e., not a vowel), remove the first
# letter and append it to the end, then add "ma".
#
# For example, the word "goat" becomes "oatgma".
#
# Constraints:
#
# 1 <= sentence.length <= 150
# sentence consists of English letters and spaces.
# sentence has no leading or trailing spaces.
# All the words in sentence are separated by a single space.


def to_goat_latin(sentence: str) -> str:
    # Time: O(n) where n = number of words
    # Space: O(n)
    vowels = ["a", "e", "i", "o", "u"]
    words = sentence.split(" ")
    output = ""
    for i, word in enumerate(words):
        if word[0].lower() in vowels:
            output += word + "ma"
        else:
            output += word[1:] + word[0] + "ma"
        output += "a" * (i + 1)
        if len(words) != i + 1:
            output += " "
    return output
