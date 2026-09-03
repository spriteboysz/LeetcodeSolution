#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 00:50
FileName: LCR/P4038. 计算单个区间中出现的整数数量.py
Description: 
"""
from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        cnt = 0
        for v in dic.values():
            if v[-1] - v[0] + 1 == len(v):
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countSpecialIntegers([3, 3, 1, 2, 2, 1])
    print(solution)
