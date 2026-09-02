#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 23:33
FileName: algorithm/P0160. 相交链表.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        curr = headA
        while curr:
            nodes.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in nodes:
                return curr
            curr = curr.next
        return None


if __name__ == '__main__':
    solution = Solution().getIntersectionNode(
        ListNode([4, 1, 8, 4, 5]),
        ListNode([5, 6, 1, 8, 4, 5])
    )
    print(solution)
