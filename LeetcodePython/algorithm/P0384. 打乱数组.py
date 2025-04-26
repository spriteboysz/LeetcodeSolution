#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 17:03
FileName: algorithm/P0384. 打乱数组.py
Description: 
"""
import random
from typing import List

from icecream import ic


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums.copy()
        random.shuffle(nums)
        return nums


if __name__ == '__main__':
    solution = Solution([1, 2, 3])
    ic(solution.shuffle())
    ic(solution.shuffle())
    ic(solution.reset())
    ic(solution.shuffle())
