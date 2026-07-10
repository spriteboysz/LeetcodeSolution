#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:26
FileName: P2130. 链表最大孪生和.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        fast = slow = head
        nums = []
        while fast and fast.next:
            nums.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        maximum = -1
        while slow:
            maximum = max(maximum, nums.pop() + slow.val)
            slow = slow.next
        return maximum


if __name__ == '__main__':
    solution = Solution().pairSum(ListNode([5, 4, 2, 1]))
    print(solution)
