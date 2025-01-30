#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 10:12
FileName: P1304. 和为零的 N 个不同整数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        for i in range(1, n // 2 + 1):
            nums.append(i)
            nums.append(-i)
        if n % 2 == 1:
            nums.append(0)
        return nums


if __name__ == '__main__':
    solution = Solution().sumZero(5)
    ic(solution)
