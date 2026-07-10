#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:02
FileName: P2610. 转换二维数组.py
Description:
"""
from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)
        maximum = max(counter.values())
        matrix = [[] for _ in range(maximum)]
        for num, cnt in counter.items():
            for i in range(cnt):
                matrix[i].append(num)
        return matrix


if __name__ == '__main__':
    solution = Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1])
    print(solution)
