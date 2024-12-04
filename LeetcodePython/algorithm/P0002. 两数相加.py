#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-03 22:45
FileName: P0002. 两数相加
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
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
    l1 = ListNode().create('[2,4,3]')
    l2 = ListNode().create('[5,6,4]')
    solution = Solution().addTwoNumbers(l1, l2)
    print(solution)
