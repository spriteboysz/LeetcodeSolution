#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 22:04
FileName: algorithm/P2527. 查询数组异或美丽值.py
Description: 
"""
from typing import List

from icecream import ic
from functools import reduce


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    solution = Solution().xorBeauty(nums=[15, 45, 20, 2, 34, 35, 5, 44, 32, 30])
    ic(solution)
