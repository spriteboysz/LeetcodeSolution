#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 12:55
FileName: P3217. 从链表中移除在数组中存在的节点.py
Description:
"""
from typing import List, Optional

from utils.node import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = curr = ListNode(-1)
        seen = set(nums)
        while head:
            if head.val not in seen:
                curr.next = head
                curr = curr.next
            else:
                if not head.next:
                    curr.next = None
            head = head.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution().modifiedList([1, 2, 3], ListNode([1, 2, 3, 4, 5]))
    print(solution)
