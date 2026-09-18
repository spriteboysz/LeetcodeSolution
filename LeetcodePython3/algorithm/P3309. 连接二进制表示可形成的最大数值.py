#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 15:08
FileName: algorithm/P3309. 连接二进制表示可形成的最大数值.py
Description: 
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def cmp(a, b):
            a, b = bin(a)[2:], bin(b)[2:]
            if a + b == b + a:
                return 0
            return -1 if int(a + b, 2) > int(b + a, 2) else 1

        nums = sorted(nums, key=cmp_to_key(cmp))
        return int(''.join(bin(num)[2:] for num in nums), 2)


if __name__ == '__main__':
    solution = Solution().maxGoodNumber(nums=[1, 2, 3])
    print('<None>' if solution is None else f'{solution=}')
