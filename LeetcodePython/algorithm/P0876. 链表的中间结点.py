#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:53
FileName: P0876. 链表的中间结点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr, n = head, 0
        while curr:
            n += 1
            curr = curr.next
        curr, i = head, 0
        while curr:
            if i == n // 2:
                return curr
            i += 1
            curr = curr.next
        return None


if __name__ == '__main__':
    head = ListNode().create('[1,2,3,4,5]')
    solution = Solution().middleNode(head)
    print(solution)
