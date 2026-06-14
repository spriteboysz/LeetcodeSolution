#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:30
FileName: P0832. 翻转图像.py
Description:
"""
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        for i, row in enumerate(image):
            for j, num in enumerate(row):
                image[i][j] = 1 - num
        return image


if __name__ == '__main__':
    solution = Solution().flipAndInvertImage(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
    print(solution)
