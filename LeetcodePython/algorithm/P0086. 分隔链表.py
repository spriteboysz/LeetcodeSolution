#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 22:04
FileName: P0086. 分隔链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        nodes1, nodes2 = [], []
        while head:
            if int(head.val) < x:
                nodes1.append(head)
            else:
                nodes2.append(head)
            head = head.next
        nodes1.extend(nodes2)
        for i in range(len(nodes1)-1):
            nodes1[i].next = nodes1[i + 1]
        nodes1[-1].next = None
        return nodes1[0]


if __name__ == '__main__':
    head = ListNode.create('[1,4,3,2,5,2]')
    solution = Solution().partition(head, 3)
    print(solution)
