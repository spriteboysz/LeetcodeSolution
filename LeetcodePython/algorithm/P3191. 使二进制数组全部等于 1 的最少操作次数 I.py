#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 17:21
FileName: P3191. 使二进制数组全部等于 1 的最少操作次数 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue
            cnt += 1
            for j in range(3):
                nums[i + j] = 1 - nums[i + j]
        if 0 in nums[-2:]:
            return -1
        return cnt


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[0, 1, 1, 1, 0, 0])
    ic(solution)
