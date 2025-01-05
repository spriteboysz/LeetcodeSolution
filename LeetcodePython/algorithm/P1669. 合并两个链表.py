#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 20:02
FileName: P1669. 合并两个链表
Description:
"""

from icecream import ic

from utils.node import ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodes1, nodes2 = [], []
        while list1:
            nodes1.append(list1)
            list1 = list1.next
        while list2:
            nodes2.append(list2)
            list2 = list2.next
        nodes1[a:b + 1] = nodes2
        for i in range(len(nodes1) - 1):
            nodes1[i].next = nodes1[i + 1]
        nodes1[-1].next = None
        return nodes1[0]


if __name__ == '__main__':
    list1 = ListNode.create('[10,1,13,6,9,5]')
    list2 = ListNode.create('[1000000,1000001,1000002]')
    solution = Solution().mergeInBetween(list1, 3, 4, list2)
    ic(solution.__str__())
