#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-10 22:57
FileName: algorithm/P2487. 从链表中移除节点.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes2 = [nodes[-1]]
        for node in nodes[:-1][::-1]:
            if node.val >= nodes2[-1].val:
                nodes2.append(node)
        nodes2.reverse()
        for i in range(1, len(nodes2)):
            nodes2[i - 1].next = nodes2[i]
        nodes2[-1].next = None
        return nodes2[0]


if __name__ == '__main__':
    h = ListNode.create('[1,2]')
    solution = Solution().removeNodes(h)
    ic(solution.__str__())
