#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 11:54
FileName: P3701. 计算交替和.py
Description:
"""
from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[::2]) - sum(nums[1::2])


if __name__ == '__main__':
    s = Solution().alternatingSum(nums=[1, 3, 5, 7])
    print(s)
