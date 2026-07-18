#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:25
FileName: P0382. 链表随机节点.py
Description:
"""
import random
from typing import Optional

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
    solution = Solution(ListNode([1, 2, 3, 4]))
    print(solution.getRandom())
