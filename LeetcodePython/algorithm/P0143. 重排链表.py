#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 23:06
FileName: P0143. 重排链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, curr = [], head
        while curr:
            nodes.append(curr)
            curr = curr.next
        n = len(nodes)
        nodes[::2], nodes[1::2] = nodes[:(n + 1) // 2], nodes[(n + 1) // 2:][::-1]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        if nodes:
            nodes[-1].next = None
        print(nodes[0])


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4]')
    Solution().reorderList(head)
