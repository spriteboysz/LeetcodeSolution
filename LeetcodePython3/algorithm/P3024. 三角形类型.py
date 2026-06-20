#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 19:06
FileName: P3024. 三角形类型.py
Description:
"""
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums, reverse=True)
        if a >= b + c:
            return 'none'
        if a == b == c:
            return 'equilateral'
        if b == c or a == b:
            return 'isosceles'
        return 'scalene'


if __name__ == '__main__':
    solution = Solution().triangleType(nums=[3, 4, 5])
    print(solution)
