#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 15:32
FileName: 面试题/面试题 16.19. 水域大小.py
Description: 
"""
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m) or land[x][y] > 0:
                return 0
            size = 1
            land[x][y] = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    size += dfs(x + dx, y + dy)
            return size

        sizes = []
        n, m = len(land), len(land[0])
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    sizes.append(dfs(i, j))
        return sorted(sizes)


if __name__ == '__main__':
    solution = Solution().pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ])
    print('<None>' if not solution else f'{solution=}')
