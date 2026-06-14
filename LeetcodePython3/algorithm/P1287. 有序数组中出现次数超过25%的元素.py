#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:22
FileName: P1287. 有序数组中出现次数超过25%的元素.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for k, v in counter.items():
            if v > len(arr) * 0.25:
                return k
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10])
    print(solution)
