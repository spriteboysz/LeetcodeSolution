#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:12
FileName: P0137. 只出现一次的数字 II.py
Description:
"""
from typing import List, Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num, cnt in counter.items():
            if cnt == 1:
                return num
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99])
    print(solution)
