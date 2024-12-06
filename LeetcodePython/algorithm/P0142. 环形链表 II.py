#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 23:03
FileName: P0142. 环形链表 II
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
