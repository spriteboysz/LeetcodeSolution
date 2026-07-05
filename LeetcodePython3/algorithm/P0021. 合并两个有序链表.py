#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-05 23:39
FileName: P0021. 合并两个有序链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next


if __name__ == '__main__':
    solution = Solution().mergeTwoLists(ListNode([1, 2, 4]), ListNode([1, 3, 4, 5]))
    print(solution)
