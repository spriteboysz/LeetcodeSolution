#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:56
FileName: algorithm/P3010. 将数组分成最小总代价的子数组 I.py
Description: 
"""
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


if __name__ == '__main__':
    solution = Solution().minimumCost([10, 3, 1, 1])
    print('<None>' if solution is None else f'{solution=}')
