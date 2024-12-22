#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:01
FileName: 面试题 02.06. 回文链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == '__main__':
    head = ListNode.create('[1,2,2,1]')
    solution = Solution().isPalindrome(head)
    print(solution)
