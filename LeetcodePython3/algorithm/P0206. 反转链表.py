#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:01
FileName: P0206. 反转链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node1, node2 = head, head.next
        dummy = self.reverseList(node2)
        node2.next = node1
        node1.next = None
        return dummy


if __name__ == '__main__':
    solution = Solution().reverseList(ListNode([1, 2, 3, 4, 5]))
    print(solution)
