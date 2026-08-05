#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 23:26
FileName: P3232. 判断是否可以赢得数字游戏.py
Description:
"""
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1, sum2 = 0, 0
        for num in nums:
            if num < 10:
                sum1 += num
            else:
                sum2 += num
        return sum1 != sum2


if __name__ == '__main__':
    solution = Solution().canAliceWin([1, 2, 3, 4, 10])
    print(solution)
