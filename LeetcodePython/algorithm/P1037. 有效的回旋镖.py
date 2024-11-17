#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 16:55
FileName: P1037. 有效的回旋镖
Description:
"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        return (b[0] - a[0]) * (c[1] - a[1]) != (c[0] - a[0]) * (b[1] - a[1])


if __name__ == '__main__':
    solution = Solution().isBoomerang(points=[[1, 1], [2, 3], [3, 2]])
    print(solution)
