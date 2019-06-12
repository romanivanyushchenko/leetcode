"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
import unittest


def get_substring_len(s: str, start: int):
    a = dict()
    for i, c in enumerate(s[start:]):
        prev = a.get(c)
        if prev is not None:
            return len(s[start:i + start]), prev + start + 1
        a[c] = i
    return len(s[start:]), -1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_len, start = get_substring_len(s, 0)
        result = substring_len

        while start > 0:
            substring_len, start = get_substring_len(s, start)
            if substring_len > result:
                result = substring_len

        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbb'), 1)

    def test_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('pwwkew'), 3)

    def test_4(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('ohomm'), 3)


if __name__ == '__main__':
    unittest.main()
