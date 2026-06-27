#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:45
FileName: P1984. 学生分数的最小差值.py
Description:
"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min((nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1)), default=nums[-1] - nums[0])


if __name__ == '__main__':
    solution = Solution().minimumDifference(nums=[9, 4, 1, 7], k=2)
    print(solution)
