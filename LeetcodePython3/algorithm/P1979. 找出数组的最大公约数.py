#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:42
FileName: P1979. 找出数组的最大公约数.py
Description:
"""
from math import gcd
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        return gcd(maximum, minimum)


if __name__ == '__main__':
    solution = Solution().findGCD(nums=[2, 5, 6, 9, 10])
    print(solution)
