#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:35
FileName: LC/LCR 136. 删除链表的节点.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur.val != val:
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().deleteNode(ListNode([1, 4, 5, 9]), 5)
    print(solution)
