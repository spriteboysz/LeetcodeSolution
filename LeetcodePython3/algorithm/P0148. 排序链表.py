#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 12:52
FileName: P0148. 排序链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda n: n.val)
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    solution = Solution().sortList(ListNode([4, 3, 1, 2]))
    print(solution)
