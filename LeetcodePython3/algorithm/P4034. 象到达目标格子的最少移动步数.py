#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 14:38
FileName: algorithm/P4034. 象到达目标格子的最少移动步数.py
Description: 
"""


class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if sum(source) % 2 != sum(target) % 2:
            return -1
        if sum(source) == sum(target) or source[0] - source[1] == target[0] - target[1]:
            return 1
        return 2


if __name__ == '__main__':
    solution = Solution().minBishopMoves(source=[4, 2], target=[1, 3])
    print('<None>' if solution is None else f'{solution=}')
