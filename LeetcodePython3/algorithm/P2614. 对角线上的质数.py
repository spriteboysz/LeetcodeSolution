#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:34
FileName: P2614. 对角线上的质数.py
Description:
"""
from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def check(n):
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        diagnose = []
        for i, row in enumerate(nums):
            diagnose.extend([row[i], row[-1 - i]])
        diagnose.sort(reverse=True)
        for num in diagnose:
            if check(num):
                return num
        return 0


if __name__ == '__main__':
    solution = Solution().diagonalPrime(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]])
    print(solution)
