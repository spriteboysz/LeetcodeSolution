#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:44
FileName: P2455. 可被三整除的偶数的平均值.py
Description:
"""
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num %  6 == 0]
        if not nums:
            return 0
        return sum(nums) // len(nums)


if __name__ == '__main__':
    solution = Solution().averageValue(nums = [1,3,6,10,12,15])
    print(solution)
