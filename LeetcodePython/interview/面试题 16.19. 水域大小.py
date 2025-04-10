#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-09 23:32
FileName: interview/面试题 16.19. 水域大小.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def dfs(x, y):
            if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or land[x][y] != 0:
                return 0
            size = 1
            land[x][y] = -1
            for dx, dy in directions:
                size += dfs(x + dx, y + dy)
            return size

        sizes = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] != 0:
                    continue
                sizes.append(dfs(i, j))
        return sorted(sizes)


if __name__ == '__main__':
    solution = Solution().pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ])
    ic(solution)
