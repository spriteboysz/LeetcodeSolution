#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 11:00
FileName: algorithm/P1980. 找出不同的二进制字符串.py
Description: 
"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        n = len(nums)
        for i in range(2 ** n):
            if (ss := bin(i)[2:].zfill(n)) not in seen:
                return ss
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().findDifferentBinaryString(nums=["111", "011", "001"])
    print('<None>' if solution is None else f'{solution=}')
