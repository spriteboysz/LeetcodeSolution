#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 10:26
FileName: LC/LCR 123. 图书整理 I.py
Description: 
"""
from typing import Optional, List

from utils.node import ListNode


class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes[::-1]


if __name__ == '__main__':
    solution = Solution().reverseBookList(ListNode([1, 2, 3, 4]))
    print(solution)
