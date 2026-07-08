#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:10
FileName: P0203. 移除链表元素.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = curr = ListNode()
        curr.next = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().removeElements(ListNode([[6, 6, 6]]), 6)
    print(solution)
