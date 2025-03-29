#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-29 22:16
FileName: interview/面试题 08.10. 颜色填充.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(x, y, old, new):
            if 0 <= x < len(image) and 0 <= y < len(image[0]):
                if image[x][y] == old:
                    image[x][y] = new
                    fill(x + 1, y, old, new)
                    fill(x - 1, y, old, new)
                    fill(x, y + 1, old, new)
                    fill(x, y - 1, old, new)

        if image[sr][sc] == newColor:
            return image
        fill(sr, sc, image[sr][sc], newColor)
        return image


if __name__ == '__main__':
    solution = Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2)
    ic(solution)
