#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 22:57
FileName: P3512. 使数组和能被 K 整除的最少操作次数.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[3, 9, 7], k=5)
    print(solution)
