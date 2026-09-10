#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 11:38
FileName: 面试题/面试题 02.05. 链表求和.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, mod = divmod(carry, 10)
            curr.next = ListNode(mod)
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().addTwoNumbers(
        l1=ListNode([7, 1, 6]), l2=ListNode([5, 9, 2])
    )
    print('<None>' if not solution else f'{solution=}')
