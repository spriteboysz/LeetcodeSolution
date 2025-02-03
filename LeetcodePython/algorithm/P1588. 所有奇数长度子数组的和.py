#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 20:46
FileName: P1588. 所有奇数长度子数组的和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ss = 0
        for n in range(1, len(arr) + 1, 2):
            for start in range(len(arr) - n + 1):
                ss += sum(arr[start:start + n])
        return ss


if __name__ == '__main__':
    solution = Solution().sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3])
    ic(solution)
