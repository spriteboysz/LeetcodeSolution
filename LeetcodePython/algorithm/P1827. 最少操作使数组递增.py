#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 16:54
FileName: P1827. 最少操作使数组递增
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt, curr = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] > curr:
                curr = nums[i]
            else:
                cnt += curr - nums[i] + 1
                curr += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[1, 5, 2, 4, 1])
    ic(solution)
