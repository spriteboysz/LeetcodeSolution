#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-03 22:59
FileName: algorithm/P0661. 图片平滑器.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def calc(x, y):
            ss, cnt = 0, 0
            for dx in range(x - 1, x + 2):
                for dy in range(y - 1, y + 2):
                    if dx < 0 or dx >= m or dy < 0 or dy >= n:
                        continue
                    ss += img[dx][dy]
                    cnt += 1
            return ss // cnt

        smoother = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                smoother[i][j] = calc(i, j)
        return smoother


if __name__ == '__main__':
    solution = Solution().imageSmoother(img=[[100, 200, 100], [200, 50, 200], [100, 200, 100]])
    ic(solution)
