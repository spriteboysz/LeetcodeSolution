#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 20:29
FileName: P2181. 合并零之间的节点
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def mergeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        nums, acc = [], 0
        for i in range(1, len(values)):
            if values[i] == 0:
                nums.append(acc)
                acc = 0
            else:
                acc += values[i]
        dummy = curr = ListNode(-1)
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        acc = 0
        dummy = curr = ListNode(-1)
        while head:
            if head.val == 0:
                head.val = acc
                curr.next = head
                curr = curr.next
                acc = 0
            else:
                acc += head.val
            head = head.next
        return dummy.next.next


if __name__ == '__main__':
    head = ListNode.create('[0,3,1,0,4,5,2,0]')
    solution = Solution().mergeNodes(head)
    ic(solution.__str__())
