#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 11:03
FileName: LCR/LCR 146. 螺旋遍历二维数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        nums = []
        while array:
            nums.extend(array[0])
            array = [list(row) for row in zip(*array[1:])][::-1]
        return nums


if __name__ == '__main__':
    solution = Solution().spiralArray(array=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
    ic(solution)
