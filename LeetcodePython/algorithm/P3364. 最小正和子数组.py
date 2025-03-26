#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-25 23:33
FileName: algorithm/P3364. 最小正和子数组.py
Description: 
"""
import math
from typing import List

from icecream import ic


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minimum = math.inf
        for n in range(l, r + 1):
            for i in range(n, len(nums) + 1):
                # print(nums[i - n:i])
                ss = sum(nums[i - n:i])
                if ss > 0:
                    minimum = min(minimum, ss)
        return minimum if minimum != math.inf else -1


if __name__ == '__main__':
    solution = Solution().minimumSumSubarray(nums=[7, 3], l=2, r=3)
    ic(solution)
