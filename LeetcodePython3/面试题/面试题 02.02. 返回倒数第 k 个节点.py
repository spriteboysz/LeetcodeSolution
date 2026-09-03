#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:53
FileName: 面试题/面试题 02.02. 返回倒数第 k 个节点.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        fast = slow = head
        while fast and k:
            fast = fast.next
            k -= 1
        while fast and slow:
            fast = fast.next
            slow = slow.next
        return slow.val


if __name__ == '__main__':
    solution = Solution().kthToLast(ListNode([1, 2, 3, 4, 5]), 2)
    print(solution)
