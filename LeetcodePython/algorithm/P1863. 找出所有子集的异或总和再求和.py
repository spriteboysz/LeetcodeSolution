#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 21:46
FileName: algorithm/P1863. 找出所有子集的异或总和再求和.py
Description: 
"""
from itertools import combinations
from typing import List

from icecream import ic
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ss = 0
        for cnt in range(len(nums)):
            ss += sum(reduce(lambda x, y: x ^ y, combination, 0) for combination in combinations(nums, cnt + 1))
        return ss


if __name__ == '__main__':
    solution = Solution().subsetXORSum(nums=[5, 1, 6])
    ic(solution)
