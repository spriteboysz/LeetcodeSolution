#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:13
FileName: P0136. 只出现一次的数字.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num, cnt in Counter(nums).items():
            if cnt == 1:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[4, 1, 2, 1, 2])
    print(solution)
