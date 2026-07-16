#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-16 23:04
FileName: P0083. 删除排序链表中的重复元素.py
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr, val = head, head.val
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                val = curr.next.val
                curr = curr.next
        return head


if __name__ == '__main__':
    solution = Solution().deleteDuplicates(ListNode([1, 1, 2, 3, 3]))
    print(solution)
