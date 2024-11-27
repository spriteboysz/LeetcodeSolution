#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:17
FileName: P2441. 与对应负数同时存在的最大正整数
Description:
"""
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive = sorted([num for num in nums if num > 0], reverse=True)
        seen = set(nums)
        for num in positive:
            if -num in seen:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().findMaxK(nums=[-1, 10, 6, 7, -7, 1])
    print(solution)
