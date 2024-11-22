#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 23:11
FileName: P3232. 判断是否可以赢得数字游戏
Description:
"""
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total1 = sum([num for num in nums if num < 10])
        return total1 * 2 != sum(nums)


if __name__ == '__main__':
    solution = Solution().canAliceWin(nums=[1, 2, 3, 4, 10])
    print(solution)
