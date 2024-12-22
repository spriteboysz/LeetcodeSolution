#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:04
FileName: 面试题 02.05. 链表求和
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    head1 = ListNode.create('[6,1,7]')
    head2 = ListNode.create('[2,9,5]')
    solution = Solution().addTwoNumbers(head1, head2)
    print(solution)
