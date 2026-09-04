#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 10:50
FileName: 面试题/面试题 17.04. 消失的数字.py
Description: 
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == '__main__':
    solution = Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(solution)
