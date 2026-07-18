#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-16 23:17
FileName: P0025. K 个一组翻转链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i in range(0, len(nodes) - k + 1, k):
            nodes[i:i + k] = nodes[i:i + k][::-1]
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    solution = Solution().reverseKGroup(ListNode([1, 2, 3, 4, 5]), 2)
    print(solution)
