#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 10:15
FileName: P1995. 统计特殊四元组.py
Description:
"""
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                for k, c in enumerate(nums[j + 1:], start=j + 1):
                    cnt += nums[k + 1:].count(a + b + c)
        return cnt


if __name__ == '__main__':
    solution = Solution().countQuadruplets(nums=[1, 1, 1, 3, 5])
    print(solution)
