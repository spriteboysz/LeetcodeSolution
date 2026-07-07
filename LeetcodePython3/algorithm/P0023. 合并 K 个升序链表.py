#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 22:44
FileName: P0023. 合并 K 个升序链表.py
Description:
"""
from typing import List, Optional

from utils.node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while any(head for head in lists):
            minimum = min(head.val for head in lists if head)
            for i, head in enumerate(lists):
                if head and head.val == minimum:
                    curr.next = head
                    curr = curr.next
                    lists[i] = head.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().mergeKLists(lists=[ListNode([1, 4, 5]), ListNode([1, 3, 4]), ListNode([2, 6])])
    print(solution)
