#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:43
FileName: algorithm/P3718. 缺失的最小倍数.py
Description: 
"""
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        for i in range(1, len(nums) + 1):
            if i * k not in seen:
                return i * k
        return k * (len(nums) + 1)


if __name__ == '__main__':
    solution = Solution().missingMultiple(nums=[99], k=99)
    print('<None>' if solution is None else f'{solution=}')
