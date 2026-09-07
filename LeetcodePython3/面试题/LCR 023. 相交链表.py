#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 09:01
FileName: 面试题/LCR 023. 相交链表.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
    solution = Solution().getIntersectionNode(ListNode([1, 2, 3]), ListNode([1, 2, 3]))
    print('<None>' if not solution else f'{solution=}')
