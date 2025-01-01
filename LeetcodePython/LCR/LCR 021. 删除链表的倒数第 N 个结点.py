#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 21:17
FileName: LCR 021. 删除链表的倒数第 N 个结点
Description:
"""
from utils.node import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = dummy = ListNode(next=head)
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().removeNthFromEnd(head, 1)
    print(solution)
