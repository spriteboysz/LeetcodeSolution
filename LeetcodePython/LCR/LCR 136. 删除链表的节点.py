#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:15
FileName: LCR 136. 删除链表的节点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes = [node for node in nodes if node.val != val]
        if not nodes:
            return head
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[4,5,1,9]')
    solution = Solution().deleteNode(head, 5)
    print(solution)
