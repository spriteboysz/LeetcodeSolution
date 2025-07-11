#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-05 17:06
FileName: algorithm/P3591. 检查元素频次是否为质数.py
Description: 
"""
from functools import lru_cache
from typing import List

from icecream import ic
from collections import defaultdict


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        @lru_cache
        def check(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return any(check(num) for num in counter.values())


if __name__ == '__main__':
    solution = Solution().checkPrimeFrequency(nums=[1, 2, 3, 4, 5, 4])
    ic(solution)
