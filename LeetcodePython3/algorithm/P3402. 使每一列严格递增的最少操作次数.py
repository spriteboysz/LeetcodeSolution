#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 16:42
FileName: algorithm/P3402. 使每一列严格递增的最少操作次数.py
Description: 
"""
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cnt = 0
        for col in zip(*grid):
            nums = list(col)
            for i, num in enumerate(nums[1:], start=1):
                if num <= nums[i - 1]:
                    nums[i] = nums[i - 1] + 1
                    cnt += nums[i] - num
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumOperations(grid=[[3, 2], [1, 3], [3, 4], [0, 1]])
    print('<None>' if solution is None else f'{solution=}')
