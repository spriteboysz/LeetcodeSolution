#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 20:51
FileName: LCR 022. 环形链表 II
Description:
"""
from utils.node import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode | None:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
