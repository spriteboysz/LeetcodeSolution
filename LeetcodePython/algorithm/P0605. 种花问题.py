#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-03 22:39
FileName: P0605. 种花问题
Description:
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1]:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    print(solution)
