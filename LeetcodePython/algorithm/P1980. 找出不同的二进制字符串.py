#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 14:10
FileName: P1980. 找出不同的二进制字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        for i in range(2 ** len(nums)):
            if (s := bin(i)[2:].zfill(len(nums))) not in seen:
                return s
        return 'Error'


if __name__ == '__main__':
    solution = Solution().findDifferentBinaryString(["111", "011", "001"])
    ic(solution)
