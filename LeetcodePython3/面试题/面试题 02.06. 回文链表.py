#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:58
FileName: 面试题/面试题 02.06. 回文链表.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(ListNode([1, 2, 2, 1]))
    print('<None>' if not solution else f'{solution=}')
