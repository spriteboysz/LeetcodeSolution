#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 16:27
FileName: algorithm/P2342. 数位和相等数对的最大和.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for num in nums:
            dic[sum(int(digit) for digit in str(num))].append(num)
        return max((sum(sorted(v, reverse=True)[:2]) for v in dic.values() if len(v) > 1), default=-1)


if __name__ == '__main__':
    solution = Solution().maximumSum(nums=[18, 43, 36, 13, 7])
    print('<None>' if solution is None else f'{solution=}')
