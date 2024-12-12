#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 22:15
FileName: P0061. 旋转链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        k %= n
        nodes = nodes[n - k:] + nodes[:n - k]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().rotateRight(head, 2)
    print(solution)
