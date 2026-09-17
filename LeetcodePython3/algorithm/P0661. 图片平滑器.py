#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 10:39
FileName: algorithm/P0661. 图片平滑器.py
Description: 
"""
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def calc(x, y):
            nums = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        nums.append(img[x + dx][y + dy])
            return sum(nums) // len(nums)

        n, m = len(img), len(img[0])
        return [[calc(i, j) for j in range(m)] for i in range(n)]


if __name__ == '__main__':
    solution = Solution().imageSmoother([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]])
    print('<None>' if solution is None else f'{solution=}')
