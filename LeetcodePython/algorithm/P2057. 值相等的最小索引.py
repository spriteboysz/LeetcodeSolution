#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-09 23:11
FileName: P2057. 值相等的最小索引
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().smallestEqual(nums=[4, 3, 2, 1])
    ic(solution)
