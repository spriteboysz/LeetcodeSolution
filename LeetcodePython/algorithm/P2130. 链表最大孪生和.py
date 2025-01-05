#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 18:37
FileName: P2130. 链表最大孪生和
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return max(values[i] + values[-i - 1] for i in range(len(values) // 2))


if __name__ == '__main__':
    head = ListNode.create('[4,2,2,3]')
    solution = Solution().pairSum(head)
    ic(solution)
