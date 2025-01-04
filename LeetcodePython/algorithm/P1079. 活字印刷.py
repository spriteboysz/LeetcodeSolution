#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 17:49
FileName: P1079. 活字印刷
Description:
"""

from itertools import permutations

from icecream import ic


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 0
        for cnt in range(1, len(tiles) + 1):
            count += len({el for el in permutations(tiles, cnt)})
        return count



if __name__ == '__main__':
    solution = Solution().numTilePossibilities("AAABBC")
    ic(solution)
