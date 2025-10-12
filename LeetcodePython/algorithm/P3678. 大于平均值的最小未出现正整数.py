#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 16:22
FileName: P3678. 大于平均值的最小未出现正整数.py
Description:
"""
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        v = sum(nums) // len(nums)
        seen = set(nums)
        for num in range(max(1, v + 1), 1000):
            if num not in seen:
                return num
        raise ValueError('Error')


if __name__ == '__main__':
    s = Solution().smallestAbsent([3, 5])
    print(s)
