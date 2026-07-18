#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:11
FileName: P0328. 奇偶链表.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        curr = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = curr
        return head


if __name__ == '__main__':
    solution = Solution().oddEvenList(ListNode([1,2,3,4,5]))
    print(solution)
