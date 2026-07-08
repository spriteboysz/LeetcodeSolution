#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:31
FileName: P0445. 两数相加 II.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    @classmethod
    def reverse_list(cls, head: ListNode | None):
        if not head or not head.next:
            return head
        node1, node2 = head, head.next
        dummy = cls.reverse_list(node2)
        node2.next = node1
        node1.next = None
        return dummy

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2, carry = self.reverse_list(l1), self.reverse_list(l2), 0
        dummy = curr = ListNode()
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
        return self.reverse_list(dummy.next)


if __name__ == '__main__':
    solution = Solution().addTwoNumbers(ListNode([7, 2, 4, 3]), ListNode([5, 6, 4]))
    print(solution)
