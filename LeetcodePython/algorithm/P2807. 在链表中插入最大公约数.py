#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 18:12
FileName: P2807. 在链表中插入最大公约数
Description:
"""
from math import gcd
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        values = []
        while head:
            values.append(head.val)
            head = head.next
        ans = sum([[value] * 2 for value in values], [])[:-1]
        for i in range(1, len(ans), 2):
            ans[i] = gcd(ans[i - 1], ans[i + 1])

        dummy = curr = ListNode(-1)
        for val in ans:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode.create('[18,6,10,3]')
    solution = Solution().insertGreatestCommonDivisors(head)
    ic(solution.__str__())
