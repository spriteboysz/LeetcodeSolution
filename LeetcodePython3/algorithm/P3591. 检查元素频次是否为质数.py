#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-23 23:55
FileName: P3591. 检查元素频次是否为质数.py
Description:
"""
from typing import List, Counter


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        primes = [True] * 100
        primes[0] = primes[1] = False
        for i in range(2, 100):
            for j in range(i * i, 100, i):
                primes[j] = False
        primes = {i for i, flag in enumerate(primes) if flag}
        counter = Counter(nums)
        return len(primes & set(counter.values())) > 0


if __name__ == '__main__':
    solution = Solution().checkPrimeFrequency(nums=[1, 2, 3, 4, 5, 4])
    print(solution)
