#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 23:25
FileName: P0142. 环形链表 II.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None


if __name__ == '__main__':
    solution = Solution().detectCycle(ListNode([3, 2, 0, -4]))
    print(solution)
