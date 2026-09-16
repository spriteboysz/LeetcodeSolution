#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-15 10:38
FileName: algorithm/P0733. 图像渲染.py
Description: 
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(x, y, c):
            if not (0 <= x < n and 0 <= y < m) or image[x][y] != c:
                return
            image[x][y] = color
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x + dx, y + dy, c)
        if image[sr][sc] == color:
            return image

        n, m = len(image), len(image[0])
        dfs(sr, sc, image[sr][sc])
        return image


if __name__ == '__main__':
    solution = Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
    print('<None>' if solution is None else f'{solution=}')
