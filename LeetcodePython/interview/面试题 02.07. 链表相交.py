#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 20:58
FileName: 面试题 02.07. 链表相交
Description:
"""
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next

        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        return None
