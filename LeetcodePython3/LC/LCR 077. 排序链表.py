#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:40
FileName: 面试题/LCR 077. 排序链表.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
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
    solution = Solution().sortList(ListNode([4, 2, 3, 1]))
    print('<None>' if not solution else f'{solution=}')
