#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:27
FileName: LC/LCR 141. 训练计划 III.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None
        return nodes[-1]


if __name__ == '__main__':
    solution = Solution().trainningPlan(ListNode([1, 2, 3, 4, 5]))
    print(solution)
