#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-02 22:58
FileName: LCR 026. 重排链表
Description:
"""
from utils.node import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, curr = [], head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes2, n = [], len(nodes)
        for i in range(n // 2 + 1):
            nodes2.append(nodes[i])
            nodes2.append(nodes[n - 1 - i])
        for i in range(len(nodes) - 1):
            nodes2[i].next = nodes2[i + 1]
        nodes2[n - 1].next = None
        print(head)


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    Solution().reorderList(head)
