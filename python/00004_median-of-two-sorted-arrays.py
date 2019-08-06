"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
import unittest
from typing import List, Tuple


def concatenate(nums1: List[int], nums2: List[int]) -> List[int]:
    ret_val = []
    idx1 = 0
    idx2 = 0

    l1 = len(nums1)
    l2 = len(nums2)

    while idx1 < l1 and idx2 < l2:
        val1 = nums1[idx1]
        val2 = nums2[idx2]

        if val1 < val2:
            ret_val.append(val1)
            idx1 += 1
        else:
            ret_val.append(val2)
            idx2 += 1

    if idx1 == l1 and idx2 < l2:
        for i in range(idx2, l2, 1):
            ret_val.append(nums2[i])

    if idx2 == l2 and idx1 < l1:
        for i in range(idx1, l1, 1):
            ret_val.append(nums1[i])

    return ret_val


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ll = len(nums1) + len(nums2)
        is_even = ll % 2 == 0
        idx = (ll//2 - 1, ll//2,) if is_even else ((ll-1)//2, (ll-1)//2)
        c = concatenate(nums1, nums2)
        values = (c[idx[0]], c[idx[1]],)
        return (values[0] + values[1]) / 2


def get_idx(nums1: List[int], nums2: List[int]) -> Tuple[int, int]:
    ll = len(nums1) + len(nums2)
    is_even = ll % 2 == 0
    idx = (ll // 2 - 1, ll // 2,) if is_even else ((ll - 1) // 2, (ll - 1) // 2)
    return idx


def get_vals(nums1: List[int], nums2: List[int]) -> Tuple[int, int]:
    idx1 = 0
    idx2 = 0
    idx = 0

    median_idx = get_idx(nums1, nums2)
    prev = 0
    curr = 0

    while idx <= median_idx[0] or idx <= median_idx[1]:
        val1 = nums1[idx1] if idx1 < len(nums1) else None
        val2 = nums2[idx2] if idx2 < len(nums2) else None

        prev = curr

        if val1 is None:
            idx2 += 1
            curr = val2
        elif val2 is None:
            idx1 += 1
            curr = val1
        elif val1 < val2:
            idx1 += 1
            curr = val1
        else:
            idx2 += 1
            curr = val2

        idx += 1

    return (curr, curr,) if (len(nums1) + len(nums2)) % 2 else (prev, curr,)


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        vals = get_vals(nums1, nums2)
        return (vals[0] + vals[1]) / 2


class Test1(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2, 3], concatenate([1, 3], [2]))

    def test_2(self):
        self.assertEqual([1, 2, 3, 4], concatenate([1, 2], [3, 4]))

    def test_3(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], concatenate([1, 2, 6], [0, 3, 4, 5, 7, 8, 9]))

    def test_4(self):
        solution = Solution1()
        self.assertEqual(2.0, solution.findMedianSortedArrays([1, 3], [2]))

    def test_5(self):
        solution = Solution1()
        self.assertEqual(2.5, solution.findMedianSortedArrays([1, 2], [3, 4]))

    def test_6(self):
        solution = Solution1()
        self.assertEqual(4.5, solution.findMedianSortedArrays([1, 2, 6], [0, 3, 4, 5, 7, 8, 9]))


class Test2(unittest.TestCase):
    def test_1(self):
        self.assertEqual((2, 2), get_vals([1, 3], [2]))

    def test_2(self):
        self.assertEqual((2, 3), get_vals([1, 2], [3, 4]))

    def test_3(self):
        self.assertEqual((4, 5), get_vals([1, 2, 6], [0, 3, 4, 5, 7, 8, 9]))

    def test_4(self):
        solution = Solution2()
        self.assertEqual(2.0, solution.findMedianSortedArrays([1, 3], [2]))

    def test_5(self):
        solution = Solution2()
        self.assertEqual(2.5, solution.findMedianSortedArrays([1, 2], [3, 4]))

    def test_6(self):
        solution = Solution2()
        self.assertEqual(4.5, solution.findMedianSortedArrays([1, 2, 6], [0, 3, 4, 5, 7, 8, 9]))


if __name__ == '__main__':
    unittest.main()
