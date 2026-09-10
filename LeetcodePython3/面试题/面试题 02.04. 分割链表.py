#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 11:44
FileName: 面试题/面试题 02.04. 分割链表.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        curr1, curr2 = dummy1, dummy2
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
        curr1.next = dummy2.next
        curr2.next = None
        return dummy1.next


if __name__ == '__main__':
    solution = Solution().partition(ListNode([1, 4, 3, 2, 5, 2]), 3)
    print('<None>' if not solution else f'{solution=}')
