#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:11
FileName: P2778. 特殊元素平方和.py
Description:
"""
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num * num for i, num in enumerate(nums) if len(nums) % (i + 1) == 0)


if __name__ == '__main__':
    solution = Solution().sumOfSquares([1, 2, 3, 4])
    print(solution)
