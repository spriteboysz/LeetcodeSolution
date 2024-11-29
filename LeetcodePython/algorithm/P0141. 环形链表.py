#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:29
FileName: P0141. 环形链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    head = ListNode().create('[3,2,0,-4]')
    solution = Solution().hasCycle(head)
    print(solution)
