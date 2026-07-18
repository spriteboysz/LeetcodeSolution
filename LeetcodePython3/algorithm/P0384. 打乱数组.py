#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:28
FileName: P0384. 打乱数组.py
Description:
"""
import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.init = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        return self.init

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


if __name__ == '__main__':
    solution = Solution([1, 2, 3, 4])
    print(solution.reset())
    print(solution.shuffle())
    print(solution.reset())
