#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 12:12
FileName: P0876. 链表的中间结点.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = Solution().middleNode(ListNode([1, 2, 3, 4, 5, 6]))
    print(solution)
