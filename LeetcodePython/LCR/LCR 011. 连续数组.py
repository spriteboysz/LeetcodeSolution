#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 17:34
FileName: LCR/LCR 011. 连续数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maximum, acc, dic = 0, 0, {0: -1}
        for i, num in enumerate(nums):
            acc += num if num == 1 else -1
            if acc in dic:
                maximum = max(maximum, i - dic[acc])
            else:
                dic[acc] = i
        return maximum


if __name__ == '__main__':
    solution = Solution().findMaxLength([0, 1, 0, 1])
    ic(solution)
