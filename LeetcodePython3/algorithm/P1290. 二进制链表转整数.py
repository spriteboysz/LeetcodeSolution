#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:37
FileName: P1290. 二进制链表转整数.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        if not head:
            return num
        while head:
            num = num * 2 + head.val
            head = head.next
        return num


if __name__ == '__main__':
    solution = Solution().getDecimalValue(ListNode([1, 0, 0, 1]))
    print(solution)
