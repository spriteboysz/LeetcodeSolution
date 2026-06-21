#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 15:13
FileName: P3866. 找到第一个唯一偶数.py
Description:
"""
from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counter = Counter(nums)
        for num in nums:
            if num % 2 == 0 and counter.get(num, 0) == 1:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().firstUniqueEven(nums=[3, 4, 2, 5, 4, 6])
    print(solution)
