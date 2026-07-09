#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 22:50
FileName: P2807. 在链表中插入最大公约数.py
Description:
"""
import math
from typing import Optional

from utils.node import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            v = math.gcd(curr.val, curr.next.val)
            node = ListNode(v, curr.next)
            curr.next = node
            curr = curr.next.next
        return head


if __name__ == '__main__':
    solution = Solution().insertGreatestCommonDivisors(ListNode([18, 6, 10, 3]))
    print(solution)
