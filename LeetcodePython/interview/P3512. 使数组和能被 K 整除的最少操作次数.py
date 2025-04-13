#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-13 23:09
FileName: interview/P3512. 使数组和能被 K 整除的最少操作次数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


if __name__ == '__main__':
    solution = Solution().minOperations(nums = [3,9,7], k = 5)
    ic(solution)
