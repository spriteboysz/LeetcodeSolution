#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-08 09:27
FileName: algorithm/P3309. 连接二进制表示可形成的最大数值.py
Description: 
"""
from itertools import permutations
from typing import List

from icecream import ic


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        maximum = 0
        for permutation in permutations(nums):
            ss = ''.join(bin(num)[2:] for num in permutation)
            curr = int(ss, 2)
            maximum = max(maximum, curr)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxGoodNumber([2, 8, 16])
    ic(solution)
