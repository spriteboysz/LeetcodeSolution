#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 22:50
FileName: P0024. 两两交换链表中的节点.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node1 = head
        node2 = head.next
        node3 = node2.next
        node1.next = self.swapPairs(node3)
        node2.next = node1
        return node2


if __name__ == '__main__':
    solution = Solution().swapPairs(ListNode([1, 2, 3, 4]))
    print(solution)
