#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:44
FileName: P0206. 反转链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i, node in enumerate(nodes[::-1][:-1]):
            node.next = nodes[len(nodes) - 2 - i]
        nodes[0].next = None
        return nodes[-1]


if __name__ == '__main__':
    head = ListNode().create('[1,2,3,4,5]')
    solution = Solution().reverseList(head)
    print(solution)
