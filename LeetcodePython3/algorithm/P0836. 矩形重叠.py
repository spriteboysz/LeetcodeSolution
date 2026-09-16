#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-15 11:28
FileName: algorithm/P0836. 矩形重叠.py
Description: 
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        minimum_x, minimum_y = max(rec1[0], rec2[0]), max(rec1[1], rec2[1])
        maximum_x, maximum_y = min(rec1[2], rec2[2]), min(rec1[3], rec2[3])
        return maximum_x > minimum_x and maximum_y > minimum_y


if __name__ == '__main__':
    solution = Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3])
    print('<None>' if solution is None else f'{solution=}')
