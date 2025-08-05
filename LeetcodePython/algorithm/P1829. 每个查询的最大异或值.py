#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-13 18:52
FileName: algorithm/P1829. 每个查询的最大异或值.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor, acc = [], 0
        maximum = 2 ** maximumBit - 1
        for num in nums:
            acc ^= num
            xor.append(acc ^ maximum)
        return xor[::-1]


if __name__ == '__main__':
    solution = Solution().getMaximumXor(nums=[0, 1, 1, 3], maximumBit=2)
    ic(solution)
