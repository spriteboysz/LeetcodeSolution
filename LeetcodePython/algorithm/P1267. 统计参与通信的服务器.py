#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-24 22:35
FileName: algorithm/P1267. 统计参与通信的服务器.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, columns = [0] * len(grid), [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] += grid[i][j]
                columns[j] += grid[i][j]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if rows[i] > 1 or columns[j] > 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countServers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    ic(solution)
