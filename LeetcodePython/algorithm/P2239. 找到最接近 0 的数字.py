#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:01
FileName: P2239. 找到最接近 0 的数字
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda num: (abs(num), -num))


if __name__ == '__main__':
    solution = Solution().findClosestNumber(nums=[2, -1, 1])
    ic(solution)
