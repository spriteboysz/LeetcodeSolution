#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 22:28
FileName: P0485. 最大连续 1 的个数.py
Description:
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ss = ''.join(map(str, nums))
        return max(len(el) for el in ss.split('0'))


if __name__ == '__main__':
    solution = Solution().findMaxConsecutiveOnes(nums=[0])
    print(solution)
