#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:37
FileName: P3065. 超过阈值的最少操作数 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(num < k for num in nums)


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10)
    ic(solution)
