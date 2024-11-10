#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:40
FileName: P0021. 合并两个有序链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2


if __name__ == '__main__':
    l1 = ListNode.create('[1,2,4]')
    l2 = ListNode.create('[1,3,4]')
    solution = Solution().mergeTwoLists(l1, l2)
    print(solution)
