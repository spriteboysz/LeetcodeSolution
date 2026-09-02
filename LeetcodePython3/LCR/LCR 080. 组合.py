#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 09:59
FileName: LCR/LCR 080. 组合.py
Description: 
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        paths = []

        def backtrack(index, path):
            if len(path) == k:
                paths.append(path.copy())
                return
            for i in range(index, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return paths


if __name__ == '__main__':
    solution = Solution().combine(4, 2)
    print(solution)
