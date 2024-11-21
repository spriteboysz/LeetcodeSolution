#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:52
FileName: P0836. 矩形重叠
Description:
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        minimum_x, minimum_y = max(rec1[0], rec2[0]), max(rec1[1], rec2[1])
        maximum_x, maximum_y = min(rec1[2], rec2[2]), min(rec1[3], rec2[3])
        return maximum_x >= minimum_x and maximum_y >= minimum_y


if __name__ == '__main__':
    solution = Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3])
    print(solution)
