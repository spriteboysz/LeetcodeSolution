#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:11
FileName: P2656. K 个元素的最大和.py
Description:
"""
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        return sum(range(maximum, maximum + k))


if __name__ == '__main__':
    solution = Solution().maximizeSum(nums = [1,2,3,4,5], k = 3)
    print(solution)
