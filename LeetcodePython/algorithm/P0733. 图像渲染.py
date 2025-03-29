#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-29 22:37
FileName: interview/P0733. 图像渲染.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill(x, y):
            if 0 <= x < len(image) and 0 <= y < len(image[0]):
                if image[x][y] == old:
                    image[x][y] = color
                    fill(x - 1, y)
                    fill(x + 1, y)
                    fill(x, y - 1)
                    fill(x, y + 1)

        old = image[sr][sc]
        if old != color:
            fill(sr, sc)
        return image


if __name__ == '__main__':
    solution = Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
    ic(solution)
