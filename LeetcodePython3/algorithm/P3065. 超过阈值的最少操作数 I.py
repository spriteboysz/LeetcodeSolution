#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:05
FileName: P3065. 超过阈值的最少操作数 I.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num >= k:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10)
    print(solution)
