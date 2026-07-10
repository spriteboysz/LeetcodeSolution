#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 22:41
FileName: P2181. 合并零之间的节点.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr1, curr2 = head.next, head
        v = 0
        while curr1:
            if curr1.val != 0:
                v += curr1.val
            else:
                curr2.next = ListNode(v)
                curr2 = curr2.next
                v = 0
            curr1 = curr1.next
        return head.next


if __name__ == '__main__':
    solution = Solution().mergeNodes(ListNode([0, 3, 1, 0, 4, 5, 2, 0]))
    print(solution)
