#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:28
FileName: P0941. 有效的山脉数组.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flags = []
        for num1, num2 in pairwise(arr):
            if num1 < num2:
                flags.append(1)
            elif num1 > num2:
                flags.append(0)
            else:
                return False
        ss = ''.join(map(str, flags))
        return ss.count('10') == 1 and ss.count('01') == 0


if __name__ == '__main__':
    solution = Solution().validMountainArray([0, 3, 2, 1])
    print(solution)
