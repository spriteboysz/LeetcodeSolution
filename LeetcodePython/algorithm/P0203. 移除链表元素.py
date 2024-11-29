#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:38
FileName: P0203. 移除链表元素
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode().create('[1,2,6,3,4,5,6]')
    solution = Solution().removeElements(head, 6)
    print(solution)
