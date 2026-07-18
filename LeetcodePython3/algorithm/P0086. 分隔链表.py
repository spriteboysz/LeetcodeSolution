#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-16 23:23
FileName: P0086. 分隔链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        small_dummy, big_dummy = ListNode(0), ListNode(0)
        small, big = small_dummy, big_dummy
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = big_dummy.next
        big.next = None
        return small_dummy.next


if __name__ == '__main__':
    solution = Solution().partition(ListNode([1, 4, 3, 2, 5, 2]), 2)
    print(solution)
