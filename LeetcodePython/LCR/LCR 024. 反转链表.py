#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:33
FileName: LCR 024. 反转链表
Description:
"""
from utils.node import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None
        return nodes[-1]


if __name__ == '__main__':
    head = ListNode.create([1, 2, 3, 4, 5])
    solution = Solution().reverseList(head)
    print(solution)
