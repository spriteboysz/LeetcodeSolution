#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 22:21
FileName: P0445. 两数相加 II
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(head):
            num = 0
            while head:
                num = num * 10 + head.val
                head = head.next
            return num

        num = dfs(l1) + dfs(l2)
        dummy = curr = ListNode(-1)
        for digit in map(int, list(str(num))):
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode.create('[7,2,4,3]')
    l2 = ListNode.create('[5,6,4]')
    solution = Solution().addTwoNumbers(l1, l2)
    print(solution)
