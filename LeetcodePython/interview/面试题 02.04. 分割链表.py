#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 20:35
FileName: 面试题 02.04. 分割链表
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        lt, gt = [], []
        while head:
            if head.val < x:
                lt.append(head)
            else:
                gt.append(head)
            head = head.next
        lt.extend(gt)
        for i in range(len(lt) - 1):
            lt[i].next = lt[i + 1]
        lt[-1].next = None
        return lt[0]


if __name__ == '__main__':
    head = ListNode.create('[1,4,3,2,5,2]')
    solution = Solution().partition(head, 3)
    print(solution)
