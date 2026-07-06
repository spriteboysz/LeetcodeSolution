#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 22:39
FileName: P0141. 环形链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    solution = Solution().hasCycle(ListNode([3, 2, 0, -4]))
    print(solution)
