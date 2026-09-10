#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 13:13
FileName: 面试题/面试题 02.01. 移除重复节点.py
Description: 
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        curr = dummy
        seen = set()
        while head:
            if head.val not in seen:
                curr.next = head
                curr = curr.next
                seen.add(head.val)
            head = head.next
        curr.next = None
        return dummy.next


if __name__ == '__main__':
    solution = Solution().removeDuplicateNodes(ListNode([1, 2, 3, 3, 2, 1]))
    print('<None>' if not solution else f'{solution=}')
