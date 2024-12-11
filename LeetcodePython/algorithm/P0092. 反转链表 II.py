#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 21:54
FileName: P0092. 反转链表 II
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes[left - 1:right] = nodes[left - 1:right][::-1]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().reverseBetween(head, 2, 4)
    print(solution)
