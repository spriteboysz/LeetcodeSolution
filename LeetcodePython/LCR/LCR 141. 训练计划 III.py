#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 11:43
FileName: LCR 141. 训练计划 III
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.reverse()
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().trainningPlan(head)
    print(solution)
