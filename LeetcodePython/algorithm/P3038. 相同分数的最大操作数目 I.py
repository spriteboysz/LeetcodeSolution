#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 21:53
FileName: P3038. 相同分数的最大操作数目 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        target = sum(nums[:2])
        cnt = 0
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums) and nums[i] + nums[i + 1] == target:
                cnt += 1
            else:
                break
        return cnt


if __name__ == '__main__':
    solution = Solution().maxOperations(nums=[3, 2, 1, 4, 5])
    ic(solution)
