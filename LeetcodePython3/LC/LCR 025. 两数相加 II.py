#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:05
FileName: LC/LCR 025. 两数相加 II.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            if not head or not head.next:
                return head
            node1, node2 = head, head.next
            dummy1 = reverse(node2)
            node2.next = node1
            node1.next = None
            return dummy1

        l1, l2 = reverse(l1), reverse(l2)
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
        return reverse(dummy.next)


if __name__ == '__main__':
    solution = Solution().addTwoNumbers(
        ListNode([7, 2, 4, 3]), ListNode([5, 6, 4])
    )
    print(solution)
