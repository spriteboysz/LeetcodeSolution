#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:35
FileName: P2733. 既不是最小值也不是最大值.py
Description:
"""
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        for num in nums:
            if num not in [maximum, minimum]:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().findNonMinOrMax([1, 2, 3, 4])
    print(solution)
