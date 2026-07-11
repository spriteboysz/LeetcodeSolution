#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:28
FileName: P1669. 合并两个链表.py
Description:
"""
from utils.node import ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1, node2 = None, None
        curr, i = list1, 0
        while curr:
            if i == a - 1:
                node1 = curr
            if i == b + 1:
                node2 = curr
            curr = curr.next
            i += 1
        node1.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = node2
        return list1


if __name__ == '__main__':
    solution = Solution().mergeInBetween(ListNode([10, 1, 13, 6, 9, 5]), 3, 4, ListNode([1000000, 1000001, 1000002]))
    print(solution)
