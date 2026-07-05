#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-02 21:46
FileName: P3701. 计算交替和.py
Description:
"""
from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[::2]) - sum(nums[1::2])


if __name__ == '__main__':
    solution = Solution().alternatingSum(nums = [1,3,5,7])
    print(solution)
