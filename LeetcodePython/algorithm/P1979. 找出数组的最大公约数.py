#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:45
FileName: P1979. 找出数组的最大公约数
Description:
"""
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        for i in range(minimum, 0, -1):
            if maximum % i == 0 and minimum % i == 0:
                return i
        return 1


if __name__ == '__main__':
    solution = Solution().findGCD(nums=[7, 5, 6, 8, 3])
    print(solution)
