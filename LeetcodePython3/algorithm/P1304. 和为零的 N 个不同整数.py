#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:12
FileName: P1304. 和为零的 N 个不同整数.py
Description:
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        if n % 2 == 1:
            nums.append(0)
        for i in range(1, n // 2 + 1):
            nums.extend([i, -i])
        return nums


if __name__ == '__main__':
    solution = Solution().sumZero(5)
    print(solution)
