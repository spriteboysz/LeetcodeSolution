#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 22:42
FileName: P1260. 二维网格迁移
Description:
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nums = [num for row in grid for num in row]
        k %= len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i * n:i * n + n] for i in range(m)]


if __name__ == '__main__':
    solution = Solution().shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4)
    print(solution)
