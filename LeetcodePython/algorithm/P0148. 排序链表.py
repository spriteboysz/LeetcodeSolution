#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 23:22
FileName: P0148. 排序链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[-1,5,3,4,0]')
    solution = Solution().sortList(head)
    print(solution)
