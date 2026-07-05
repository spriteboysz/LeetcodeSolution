#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-05 22:26
FileName: P0002. 两数相加.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += int(l1.val)
                l1 = l1.next
            if l2:
                carry += int(l2.val)
                l2 = l2.next
            carry, mod = divmod(carry, 10)
            curr.next = ListNode(mod)
            curr = curr.next
        return ans.next


if __name__ == '__main__':
    solution = Solution().addTwoNumbers(ListNode([2, 4, 3]), ListNode([5, 6, 4]))
    print(solution)
