#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-08 09:38
FileName: algorithm/P1375. 二进制字符串前缀一致的次数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt, maximum = 0, 0
        for i, num in enumerate(flips):
            maximum = max(num, maximum)
            if maximum == i + 1:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numTimesAllBlue(flips=[3, 2, 4, 1, 5])
    ic(solution)
