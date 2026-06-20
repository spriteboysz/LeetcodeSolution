#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:38
FileName: P1539. 第 k 个缺失的正整数.py
Description:
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return sorted(set(range(1, len(arr) + k + 1)) - set(arr))[k - 1]


if __name__ == '__main__':
    solution = Solution().findKthPositive(arr=[1, 2, 3, 4], k=2)
    print(solution)
