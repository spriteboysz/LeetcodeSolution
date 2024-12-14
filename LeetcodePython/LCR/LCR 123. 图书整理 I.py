#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:37
FileName: LCR 123. 图书整理 I
Description:
"""
from typing import Optional, List

from utils.node import ListNode


class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values[::-1]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().reverseBookList(head)
    print(solution)
