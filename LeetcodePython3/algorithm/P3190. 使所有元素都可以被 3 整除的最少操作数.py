#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 22:49
FileName: P3190. 使所有元素都可以被 3 整除的最少操作数.py
Description:
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(num % 3 != 0 for num in nums)


if __name__ == '__main__':
    solution = Solution().minimumOperations([1, 2, 3, 4])
    print(solution)
