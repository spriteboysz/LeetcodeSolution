#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 21:42
FileName: P0234. 回文链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(ListNode([1,2,2,1]))
    print(solution)
