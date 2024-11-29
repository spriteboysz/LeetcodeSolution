#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:16
FileName: P0083. 删除排序链表中的重复元素
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    head = ListNode().create('[1,1,2,3,3]')
    solution = Solution().deleteDuplicates(head)
    print(solution)
