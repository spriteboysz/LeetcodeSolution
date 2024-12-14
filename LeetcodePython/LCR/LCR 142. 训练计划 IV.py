#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:40
FileName: LCR 142. 训练计划 IV
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while l1:
            nodes.append(l1)
            l1 = l1.next
        while l2:
            nodes.append(l2)
            l2 = l2.next
        if not nodes:
            return l1
        nodes.sort(key=lambda el: el.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    l1 = ListNode.create('[1,2,4]')
    l2 = ListNode.create('[1,3,4]')
    solution = Solution().trainningPlan(l1, l2)
    print(solution)
