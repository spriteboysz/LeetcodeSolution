#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 12:02
FileName: P0645. 错误的集合.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        counter = Counter(nums)
        for num in range(1, len(nums) + 1):
            if counter.get(num, 0) == 2:
                num1 = num
            if counter.get(num, 0) == 0:
                num2 = num
        return [num1, num2]


if __name__ == '__main__':
    solution = Solution().findErrorNums(nums=[1, 2, 2, 4])
    print(solution)
