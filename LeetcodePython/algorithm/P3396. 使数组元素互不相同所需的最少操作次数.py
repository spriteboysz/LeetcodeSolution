#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 19:56
FileName: P3396. 使数组元素互不相同所需的最少操作次数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumOperations(nums=[1, 2, 3, 4, 2, 3, 3, 5, 7])
    ic(solution)
