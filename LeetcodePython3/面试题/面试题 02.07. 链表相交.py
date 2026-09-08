#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:01
FileName: 面试题/面试题 02.07. 链表相交.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next

        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None


if __name__ == '__main__':
    solution = Solution().getIntersectionNode(
        ListNode([1, 2, 3]), ListNode([1, 2, 3])
    )
    print('<None>' if not solution else f'{solution=}')
