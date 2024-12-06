#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 22:09
FileName: P0328. 奇偶链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        n = len(nodes)
        nodes[:(n + 1) // 2], nodes[(n + 1) // 2:] = nodes[::2], nodes[1::2]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[2,1,3,5,6,4,7]')
    solution = Solution().oddEvenList(head)
    print(solution)
