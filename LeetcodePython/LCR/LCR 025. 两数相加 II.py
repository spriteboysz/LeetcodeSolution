#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 20:54
FileName: LCR 025. 两数相加 II
Description:
"""
from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        values1, values2 = [], []
        while l1:
            values1.append(l1.val)
            l1 = l1.next
        while l2:
            values2.append(l2.val)
            l2 = l2.next
        carry, values = 0, []
        while values1 or values2 or carry:
            if values1:
                carry += values1.pop()
            if values2:
                carry += values2.pop()
            carry, mod = divmod(carry, 10)
            values.append(mod)
        values.reverse()
        dummy = curr = ListNode(-1)
        for value in values:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    head1 = ListNode.create('[7,2,4,3]')
    head2 = ListNode.create('[5,6,4]')
    solution = Solution().addTwoNumbers(head1, head2)
    print(solution)
