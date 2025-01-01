#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:28
FileName: LCR 077. 排序链表
Description:
"""
from utils.node import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        values, curr = [], head
        while curr:
            values.append(curr.val)
            curr = curr.next
        values.sort(reverse=True)
        curr = head
        while curr:
            curr.val = values.pop()
            curr = curr.next
        return head


if __name__ == '__main__':
    head = ListNode.create('[-1,5,3,4,0]')
    solution = Solution().sortList(head)
    print(solution)
