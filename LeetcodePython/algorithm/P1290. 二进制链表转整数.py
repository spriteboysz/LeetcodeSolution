#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:58
FileName: P1290. 二进制链表转整数
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = 0
        while head:
            value = value * 2 + head.val
            head = head.next
        return value


if __name__ == '__main__':
    head = ListNode().create('[1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]')
    solution = Solution().getDecimalValue(head)
    print(solution)
