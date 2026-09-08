#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:55
FileName: 面试题/面试题 02.08. 环路检测.py
Description: 
"""

from utils.node import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


if __name__ == '__main__':
    solution = Solution().detectCycle(ListNode([1, 2, 3, 4]))
    print('<None>' if not solution else f'{solution=}')
