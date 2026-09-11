#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 11:17
FileName: algorithm/P3191. 使二进制数组全部等于 1 的最少操作次数 I.py
Description: 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                cnt += 1
        return cnt if 0 not in nums[-2:] else -1


if __name__ == '__main__':
    solution = Solution().minOperations([0, 1, 1, 1, 0, 0])
    print('<None>' if solution is None else f'{solution=}')
