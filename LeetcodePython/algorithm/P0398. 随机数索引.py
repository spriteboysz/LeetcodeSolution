#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-08 09:22
FileName: algorithm/P0398. 随机数索引.py
Description: 
"""
import random
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dic.get(target))


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 3, 3])
    ic(solution.pick(3))
    ic(solution.pick(1))
    ic(solution.pick(3))
