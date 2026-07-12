#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 21:33
FileName: P2095. 删除链表的中间节点.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    solution = Solution().deleteMiddle(ListNode([1, 3, 4, 7, 1, 2, 6]))
    print(solution)
