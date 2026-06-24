#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 23:19
FileName: P1827. 最少操作使数组递增.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                cnt += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[1, 5, 2, 4, 1])
    print(solution)
