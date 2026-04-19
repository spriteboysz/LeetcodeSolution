#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-19 20:17
FileName: P3095. 或值至少 K 的最短子数组 I.py
Description:
"""
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minimum = 100
        for i, value in enumerate(nums):
            for j, num in enumerate(nums[i:]):
                value |= num
                if value >= k:
                    minimum = min(minimum, j + 1)
                    break
        return minimum if minimum != 100 else -1


if __name__ == '__main__':
    solution = Solution().minimumSubarrayLength(nums=[2, 1, 8], k=10)
    print(solution)
