#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:59
FileName: algorithm/P3678. 大于平均值的最小未出现正整数.py
Description: 
"""
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) // len(nums)
        seen = set(nums)
        while True:
            avg += 1
            if avg > 0 and avg not in seen:
                return avg


if __name__ == '__main__':
    solution = Solution().smallestAbsent([3, 5])
    print('<None>' if solution is None else f'{solution=}')
