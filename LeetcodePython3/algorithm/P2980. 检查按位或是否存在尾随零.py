#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:34
FileName: P2980. 检查按位或是否存在尾随零.py
Description:
"""
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(num % 2 == 0 for num in nums) >= 2


if __name__ == '__main__':
    solution = Solution().hasTrailingZeros(nums=[1, 2, 3, 4, 5])
    print(solution)
