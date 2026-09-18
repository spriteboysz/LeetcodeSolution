#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 14:29
FileName: algorithm/P1267. 统计参与通信的服务器.py
Description: 
"""
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    cnt += 1
        return sum(rows) - cnt


if __name__ == '__main__':
    solution = Solution().countServers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    print('<None>' if solution is None else f'{solution=}')
