#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:04
FileName: 面试题 02.05. 链表求和
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(-1), 0
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
    head1 = ListNode.create('[2,4,3]')
    head2 = ListNode.create('[1]')
    solution = Solution().addTwoNumbers(head1, head2)
    print(solution)
