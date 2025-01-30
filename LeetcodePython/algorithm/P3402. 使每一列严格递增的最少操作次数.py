#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 19:51
FileName: P3402. 使每一列严格递增的最少操作次数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in map(lambda el: list(el), zip(*grid)):
            for i in range(1, len(row)):
                if row[i] <= row[i - 1]:
                    cnt += row[i - 1] + 1 - row[i]
                    row[i] = row[i - 1] + 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumOperations(grid=[[3, 2], [1, 3], [3, 4], [0, 1]])
    ic(solution)
