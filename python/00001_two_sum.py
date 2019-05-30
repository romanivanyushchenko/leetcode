"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1:]):
                if x + y == target:
                    return [i, j + i + 1]
        return []


class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual([0, 1], solution.twoSum([2, 7, 11, 15], 9))

    def test_2(self):
        solution = Solution()
        self.assertEqual([0, 2], solution.twoSum([3, 2, 3], 6))


if __name__ == '__main__':
    unittest.main()
