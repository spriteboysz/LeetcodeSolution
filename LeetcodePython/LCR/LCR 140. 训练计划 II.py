#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 11:35
FileName: LCR 140. 训练计划 II
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        curr, n = head, 0
        while curr:
            n += 1
            curr = curr.next
        curr = head
        while n - cnt:
            curr = curr.next
            n -= 1
        return curr


if __name__ == '__main__':
    head = ListNode.create('[2,4,7,8]')
    solution = Solution().trainingPlan(head, 1)
    print(solution)
