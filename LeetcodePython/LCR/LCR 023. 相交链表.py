#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:10
FileName: LCR 023. 相交链表
Description:
"""
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        nodes = set()
        while head1:
            nodes.add(head1)
            head1 = head1.next
        while head2:
            if head2 in nodes:
                return head2
            head2 = head2.next
        return head2


if __name__ == '__main__':
    head1 = ListNode.create('[1,2,3,4]')
    head2 = ListNode.create('[1,2,3,4]')
    solution = Solution().getIntersectionNode(head1, head2)
    print(solution)
