#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 08:51
FileName: 面试题/LCR 027. 回文链表.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(ListNode([1, 2, 3, 3, 2, 1]))
    print(solution)
