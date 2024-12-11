#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-10 23:24
FileName: P0024. 两两交换链表中的节点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        n = n // 2 * 2
        nodes[:n:2], nodes[1:n:2] = nodes[1:n:2], nodes[:n:2]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3]')
    solution = Solution().swapPairs(head)
    print(solution)
