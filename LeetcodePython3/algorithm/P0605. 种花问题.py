#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:14
FileName: P0605. 种花问题.py
Description:
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if sum(flowerbed[i - 1:i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return n <= 0


if __name__ == '__main__':
    solution = Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    print(solution)
