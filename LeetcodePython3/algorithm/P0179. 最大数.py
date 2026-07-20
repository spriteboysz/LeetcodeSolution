#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 21:49
FileName: P0179. 最大数.py
Description:
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def func(num1, num2):
            a, b = num1 + num2, num2 + num1
            if a > b:
                return -1
            if a < b:
                return 1
            return 0

        ss = sorted(map(str, nums), key=cmp_to_key(func))
        if ss[0] == '0':
            return '0'
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().largestNumber(nums=[30, 3, 34, 5, 9])
    print(solution)
