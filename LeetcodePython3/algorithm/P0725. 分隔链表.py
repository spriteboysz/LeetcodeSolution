#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-20 23:08
FileName: P0725. 分隔链表.py
Description:
"""
from typing import Optional, List

from utils.node import ListNode


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        parts = [None for _ in range(k)]
        if not head:
            return parts

        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        div, mod = divmod(len(nodes), k)
        m = 0
        for i in range(k):
            parts[i] = nodes[m]
            m += div + bool(mod)
            if m >= len(nodes):
                break
            mod = mod - 1
            mod = max(mod-1, 0)
            nodes[m - 1].next = None

        return parts


if __name__ == '__main__':
    solution = Solution().splitListToParts(ListNode([1, 2, 3]), 4)
    print(solution)
