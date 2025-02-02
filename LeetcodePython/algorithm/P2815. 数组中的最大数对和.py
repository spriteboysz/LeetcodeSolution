#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 22:58
FileName: P2815. 数组中的最大数对和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximum = -1
        for j, num2 in enumerate(nums):
            for _, num1 in enumerate(nums[:j]):
                if max(str(num1)) == max(str(num2)):
                    maximum = max(maximum, num1 + num2)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSum(nums=[51, 71, 17, 24, 42])
    ic(solution)
