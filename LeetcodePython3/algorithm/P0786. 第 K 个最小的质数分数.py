#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 15:49
FileName: algorithm/P0786. 第 K 个最小的质数分数.py
Description: 
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fractions = []
        for i, num1 in enumerate(arr):
            for num2 in arr[i + 1:]:
                fractions.append([num1, num2])
        return sorted(fractions, key=lambda e: e[0] / e[1])[k - 1]


if __name__ == '__main__':
    solution = Solution().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3)
    print('<None>' if solution is None else f'{solution=}')
