#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 16:13
FileName: P3688. 偶数的按位或运算.py
Description:
"""
from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num % 2 == 0:
                res |= num
        return res


if __name__ == '__main__':
    s = Solution().evenNumberBitwiseORs(nums = [1,2,3,4,5,6])
    print(s)
