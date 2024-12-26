#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:18
FileName: P0025. K 个一组翻转链表
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
        for i in range(0, len(nodes) // k * k, k):
            nodes[i:i + k] = nodes[i:i + k][::-1]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().reverseKGroup(head, 2)
    print(solution)
