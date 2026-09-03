#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:31
FileName: LC/LCR 142. 训练计划 IV.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next


if __name__ == '__main__':
    solution = Solution().trainningPlan(
        ListNode([1, 2, 3]),
        ListNode([1, 3, 4])
    )
    print(solution)
