#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-15 22:38
FileName: P0725. 分隔链表
Description:
"""
from typing import Optional, List

from utils.node import ListNode


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        div, mod = divmod(len(nodes), k)
        lists, left = [], 0
        for i in range(k):
            m = div + int(i < mod)
            if left >= len(nodes):
                lists.append(None)
            else:
                lists.append(nodes[left])
                nodes[left + m - 1].next = None
            left += m
        return lists


if __name__ == '__main__':
    head = ListNode.create('[1,2,3]')
    solution = Solution().splitListToParts(head, 5)
    for lst in solution:
        print(lst)
