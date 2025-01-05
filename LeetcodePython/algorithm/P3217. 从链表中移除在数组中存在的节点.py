#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 18:24
FileName: P3217. 从链表中移除在数组中存在的节点
Description:
"""
from typing import List, Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        seen = set(nums)
        nodes = [node for node in nodes if node.val not in seen]

        if not nodes:
            return None
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().modifiedList([1, 2, 3], head)
    ic(solution.__str__())
