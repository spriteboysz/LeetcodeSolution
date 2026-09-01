#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:03
FileName: algorithm/P2657. 找到两个数组的前缀公共数组.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic1, dic2 = defaultdict(int), defaultdict(int)
        counters = []
        for num1, num2 in zip(A, B):
            dic1[num1] += 1
            dic2[num2] += 1
            count = 0
            for num, cnt in dic1.items():
                count += min(cnt, dic2.get(num, 0))
            counters.append(count)
        return counters


if __name__ == '__main__':
    solution = Solution().findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4])
    print(solution)
