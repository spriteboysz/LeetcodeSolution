#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:35
FileName: LC/LCR 171. 训练计划 V.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next
        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        return None


if __name__ == '__main__':
    solution = Solution().getIntersectionNode(
        ListNode([1, 2, 3]), ListNode([1, 3, 4])
    )
    print(solution)
