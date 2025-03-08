#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:38
FileName: LCR/P3375. 使数组的值全部为 K 的最少操作次数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in set(nums)):
            return -1
        return len(set(nums) - {k})


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[5, 2, 5, 4, 5], k=2)
    ic(solution)
