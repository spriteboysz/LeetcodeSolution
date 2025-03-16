#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:17
FileName: algorithm/P3483. 不同三位偶数的数目.py
Description: 
"""
from typing import List
from collections import Counter

from icecream import ic


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = 0
        counter1 = Counter(map(str, digits))
        for num in range(100, 1000, 2):
            counter = Counter(str(num))
            for k, v in counter.items():
                if v > counter1.get(str(k), 0):
                    break
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().totalNumbers(digits=[1, 2, 3, 4])
    ic(solution)
