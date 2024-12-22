#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 21:00
FileName: 面试题 02.08. 环路检测
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
