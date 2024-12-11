#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-10 23:35
FileName: P0019. 删除链表的倒数第 N 个结点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        m = len(nodes)
        nodes = nodes[:m - n] + nodes[m - n + 1:]
        if not nodes:
            return None
        for i in range(m - 2):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().removeNthFromEnd(head, 2)
    print(solution)
