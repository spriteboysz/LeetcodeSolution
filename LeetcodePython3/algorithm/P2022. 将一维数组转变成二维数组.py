#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 00:08
FileName: P2022. 将一维数组转变成二维数组.py
Description:
"""
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return [original[i:i + n] for i in range(0, m * n, n)]


if __name__ == '__main__':
    solution = Solution().construct2DArray(original=[1, 2, 3, 4], m=2, n=2)
    print(solution)
