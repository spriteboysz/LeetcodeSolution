#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-11 22:24
FileName: P0023. 合并 K 个升序链表
Description:
"""
from typing import Optional, List

from utils.node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next
        if len(nodes) == 0:
            return None
        nodes.sort(key=lambda el: el.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head1 = ListNode.create('[1,4,5]')
    head2 = ListNode.create('[1,3,4]')
    head3 = ListNode.create('[2,6]')
    solution = Solution().mergeKLists([head1, head2, head3])
    print(solution)
