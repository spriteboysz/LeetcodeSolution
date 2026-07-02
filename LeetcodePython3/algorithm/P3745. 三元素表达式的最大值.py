#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 22:58
FileName: P3745. 三元素表达式的最大值.py
Description:
"""
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a, b, *_, c = sorted(nums, reverse=True)
        return a + b - c


if __name__ == '__main__':
    solution = Solution().maximizeExpressionOfThree([1, 4, 2, 5])
    print(solution)
