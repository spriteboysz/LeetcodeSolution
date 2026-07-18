#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:47
FileName: P0398. 随机数索引.py
Description:
"""
import random
from typing import List
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dic.get(target, []))


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 3, 3])
    print(solution.pick(3))
