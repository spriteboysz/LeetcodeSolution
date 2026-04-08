#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-07 22:56
FileName: P3818. 移除前缀使数组严格递增.py
Description:
"""
from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        minimum, cur = 1, nums[-1]
        for num in nums[:-1][::-1]:
            if num >= cur:
                break
            cur = num
            minimum += 1
        return len(nums) - minimum


if __name__ == '__main__':
    solution = Solution().minimumPrefixLength(nums=[1, -1, 2, 3, 3, 4, 5])
    print(solution)
