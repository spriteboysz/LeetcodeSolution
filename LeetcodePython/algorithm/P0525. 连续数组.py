#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 17:08
FileName: algorithm/P0525. 连续数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maximum, acc, dic = 0, 0, {0: -1}
        for i, x in enumerate(nums):
            acc += 1 if x else -1
            if acc in dic:
                maximum = max(maximum, i - dic[acc])
            else:
                dic[acc] = i
            ic(maximum, acc, dic)
        return maximum


if __name__ == '__main__':
    solution = Solution().findMaxLength(nums=[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])
    ic(solution)
