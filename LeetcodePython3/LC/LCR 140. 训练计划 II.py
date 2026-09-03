#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 16:26
FileName: LC/LCR 140. 训练计划 II.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and cnt:
            fast = fast.next
            cnt -= 1
        while fast and slow:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    solution = Solution().trainingPlan(ListNode([2, 4, 7, 8]), 1)
    print(solution)
