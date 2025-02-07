#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:45
FileName: P1561. 你可以获得的最大硬币数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles) * 2 // 3:2])


if __name__ == '__main__':
    solution = Solution().maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4])
    ic(solution)
