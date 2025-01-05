#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 17:57
FileName: P1721. 交换链表中的节点
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes, curr = [], head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes[k - 1].val, nodes[-k].val = nodes[-k].val, nodes[k - 1].val
        return head


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().swapNodes(head, 2)
    ic(solution.__str__())
