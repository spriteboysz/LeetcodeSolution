#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 22:47
FileName: P0061. 旋转链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        k %= len(nodes)
        if k == 0:
            return nodes[0]
        k = len(nodes) - k

        nodes[-1].next = nodes[0]
        nodes[k - 1].next = None
        return nodes[k]


if __name__ == '__main__':
    solution = Solution().rotateRight(ListNode([1, 2, 3, 4, 5]), 2)
    print(solution)
