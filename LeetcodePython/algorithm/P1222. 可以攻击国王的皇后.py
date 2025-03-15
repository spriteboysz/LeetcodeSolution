#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 10:26
FileName: algorithm/P1222. 可以攻击国王的皇后.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        seen = set(map(tuple, queens))
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        points = []
        for dx, dy in directions:
            x, y = king[0] + dx, king[1] + dy
            while 0 <= x <= 8 and 0 <= y <= 8:
                if (x, y) in seen:
                    points.append([x, y])
                    break
                x += dx
                y += dy
        return points


if __name__ == '__main__':
    solution = Solution().queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0])
    ic(solution)
