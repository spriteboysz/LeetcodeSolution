#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 10:38
FileName: algorithm/P1222. 可以攻击国王的皇后.py
Description: 
"""
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attack = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                kx, ky = king[0] + dx, king[1] + dy
                while 0 <= kx < 8 and 0 <= ky < 8:
                    if [kx, ky] in queens:
                        attack.append([kx, ky])
                        break
                    kx += dx
                    ky += dy
        return attack


if __name__ == '__main__':
    solution = Solution().queensAttacktheKing(
        queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]],
        king=[0, 0]
    )
    print(solution)
