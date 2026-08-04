#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 16:07
FileName: P1588. 所有奇数长度子数组的和.py
Description:
"""
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i, num in enumerate(arr):
            for j in range(i, len(arr), 2):
                ans += sum(arr[i:j + 1])
        return ans


if __name__ == '__main__':
    solution = Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3])
    print(solution)
