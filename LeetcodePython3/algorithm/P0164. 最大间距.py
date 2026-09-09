#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:16
FileName: algorithm/P0164. 最大间距.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(num2 - num1 for num1, num2 in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().maximumGap([3, 6, 9, 1])
    print('<None>' if not solution else f'{solution=}')
