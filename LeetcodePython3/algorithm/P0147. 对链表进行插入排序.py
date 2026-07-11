#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 12:16
FileName: P0147. 对链表进行插入排序.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    solution = Solution().insertionSortList(ListNode([4, 1, 3, 2]))
    print(solution)
