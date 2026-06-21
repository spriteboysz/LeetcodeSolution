#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:37
FileName: P3158. 求出出现两次数字的 XOR 值.py
Description:
"""
from functools import reduce
from typing import List, Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return reduce(lambda a, b: a ^ b, [k for k, v in counter.items() if v == 2], 0)


if __name__ == '__main__':
    solution = Solution().duplicateNumbersXOR(nums=[1, 2, 2, 1])
    print(solution)
