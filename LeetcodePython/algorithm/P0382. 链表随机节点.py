#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-20 23:24
FileName: algorithm/P0382. 链表随机节点.py
Description: 
"""
import random
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.values)


if __name__ == '__main__':
    solution = Solution(ListNode.create('[1, 2, 3]'))
    ic(solution.getRandom())
    ic(solution.getRandom())
    ic(solution.getRandom())
    ic(solution.getRandom())
