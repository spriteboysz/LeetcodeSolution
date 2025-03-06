#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 22:57
FileName: algorithm/P2917. 找出数组中的 K-or 值.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for digits in zip(*map(lambda num: bin(num)[2:].zfill(32), nums)):
            ans = ans * 2 + (digits.count('1') >= k)
        return ans


if __name__ == '__main__':
    solution = Solution().findKOr(nums=[7, 12, 9, 8, 9, 15], k=4)
    ic(solution)
