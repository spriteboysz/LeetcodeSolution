#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-06 22:46
FileName: algorithm/P3637. 三段式数组 I.py
Description: 
"""
from typing import List
from itertools import pairwise

from icecream import ic


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ans = []
        for a, b in pairwise(nums):
            if a == b:
                return False
            ans.append(int(b > a))
        ss = ''.join(map(str, ans))
        return ss[0] == ss[-1] == '1' and set(ss.strip('1')) == {'0'}


if __name__ == '__main__':
    solution = Solution().isTrionic(nums=[5, 9, 1, 7])
    ic(solution)
