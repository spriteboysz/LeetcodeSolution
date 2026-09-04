#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 08:31
FileName: LC/LCR 146. 螺旋遍历二维数组.py
Description: 
"""
from typing import List


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        def rotate(grid):
            return [row for row in zip(*grid)][::-1]

        nums = []
        while array:
            nums.extend(array[0])
            array = rotate(array[1:])
        return nums


if __name__ == '__main__':
    solution = Solution().spiralArray([
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ])
    print(solution)
