"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def as_list(self):
        values = [self.val]
        node = self
        while node.next:
            node = node.next
            values.append(node.val)
        return values

    def __str__(self):
        return print(self.as_list())


def get_value(node: ListNode):
    if node:
        return node.val
    return 0


def get_sum(n1: ListNode, n2: ListNode, m: int):
    v1 = get_value(n1)
    v2 = get_value(n2)
    v = v1 + v2 + m
    return v % 10, v // 10


def new_node(n1: ListNode, n2: ListNode, m: int):
    v, m = get_sum(n1, n2, m)
    return ListNode(v), m


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2

        n, m = new_node(n1, n2, 0)
        result = n

        while (n1 and n1.next) or (n2 and n2.next):
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
            n.next, m = new_node(n1, n2, m)
            n = n.next

        if m:
            n.next = ListNode(m)

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        self.assertEqual([7, 0, 8], solution.addTwoNumbers(l1, l2).as_list())

    def test_2(self):
        l1 = ListNode(5)
        l2 = ListNode(5)

        solution = Solution()
        self.assertEqual([0, 1], solution.addTwoNumbers(l1, l2).as_list())


if __name__ == '__main__':
    unittest.main()
