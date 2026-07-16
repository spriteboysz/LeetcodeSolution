#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 22:33
FileName: P0019. 删除链表的倒数第 N 个结点.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().removeNthFromEnd(ListNode([1, 2, 3, 4, 5]), 2)
    print(solution)
