#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:26
FileName: P1431. 拥有最多糖果的孩子.py
Description:
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [candy + extraCandies >= maximum for candy in candies]


if __name__ == '__main__':
    solution = Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)
    print(solution)
