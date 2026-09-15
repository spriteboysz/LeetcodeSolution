#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 15:08
FileName: algorithm/P3637. 三段式数组 I.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ans = []
        for a, b in pairwise(nums):
            if a == b:
                return False
            ans.append(int(b > a))
        ss = ''.join(map(str, ans))
        return ss.startswith('1') and ss.endswith('1') and set(ss.strip('1')) == {'0'}


if __name__ == '__main__':
    solution = Solution().isTrionic(nums=[1, 3, 5, 4, 2, 6])
    print('<None>' if solution is None else f'{solution=}')
