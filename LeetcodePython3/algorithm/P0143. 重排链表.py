#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 12:45
FileName: P0143. 重排链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode
import math


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        m = math.ceil(len(nodes) / 2)
        nodes[::2], nodes[1::2] = nodes[:m], nodes[m:][::-1]
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i + 1]
        nodes[-1].next = None
        print(nodes[0])


if __name__ == '__main__':
    Solution().reorderList(ListNode([1, 2, 3, 4, 5]))
