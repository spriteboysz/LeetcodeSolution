#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 23:06
FileName: P3427. 变长子数组求和.py
Description:
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            start = max(0, i - num)
            ans += sum(nums[start:i + 1])
        return ans


if __name__ == '__main__':
    solution = Solution().subarraySum(nums=[2, 3, 1])
    print(solution)
