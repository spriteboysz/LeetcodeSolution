#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-15 23:12:08
LastEditTime: 2022-04-21 22:58:42
Description: 
FilePath: 605.种花问题.py
"""
#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1], 0))
