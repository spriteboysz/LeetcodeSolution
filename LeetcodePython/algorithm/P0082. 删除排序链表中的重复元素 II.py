#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 16:29
FileName: P0082. 删除排序链表中的重复元素 II
Description:
"""
from collections import Counter
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        counter = Counter(map(lambda node: node.val, nodes))
        nodes = [node for node in nodes if counter.get(node.val) == 1]
        if not nodes:
            return None
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    head = ListNode.create('[1,1]')
    solution = Solution().deleteDuplicates(head)
    print(solution)
    ic(solution)
