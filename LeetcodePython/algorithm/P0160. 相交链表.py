#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:32
FileName: P0160. 相交链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes1 = set()
        curr = headA
        while curr:
            nodes1.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in nodes1:
                return curr
            curr = curr.next
        return None


if __name__ == '__main__':
    headA = ListNode().create('[4,1,8,4,5]')
    headB = ListNode().create('[4,1,8,4,5]')
    solution = Solution().getIntersectionNode(headA, headB)
    print(solution)
