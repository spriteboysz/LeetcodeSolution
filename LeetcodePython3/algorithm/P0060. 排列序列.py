#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 22:54
FileName: algorithm/P0060. 排列序列.py
Description: 
"""
from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = list(permutations(range(1, n + 1), n))
        return ''.join(map(str, permutation[k - 1]))


if __name__ == '__main__':
    solution = Solution().getPermutation(3, 3)
    print(solution)
