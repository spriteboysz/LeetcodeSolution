#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:24
FileName: P2848. 与车相交的点
Description:
"""
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        digits = [0] * 101
        for s, e in nums:
            for i in range(s, e + 1):
                digits[i] += 1
        return sum([digit > 0 for digit in digits])


if __name__ == '__main__':
    solution = Solution().numberOfPoints(nums=[[3, 6], [1, 5], [4, 7]])
    print(solution)
