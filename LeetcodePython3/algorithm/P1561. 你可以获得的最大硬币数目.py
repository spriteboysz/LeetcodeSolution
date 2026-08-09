#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:18
FileName: P1561. 你可以获得的最大硬币数目.py
Description:
"""
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles)*2//3:2])


if __name__ == '__main__':
    solution = Solution().maxCoins(piles=[9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(solution)
