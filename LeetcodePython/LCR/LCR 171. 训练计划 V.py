#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 14:21
FileName: LCR 171. 训练计划 V
Description:
"""
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode | None:
        nodes = []
        while head1:
            nodes.append(head1)
            head1 = head1.next
        while head2:
            if head2 in nodes:
                return head2
            head2 = head2.next
        return None


if __name__ == '__main__':
    head1 = ListNode.create('[4,1,8,4,5]')
    head2 = ListNode.create('[5,0,1,8,4,5]')
    solution = Solution().getIntersectionNode(head1, head2)
    print(solution)
