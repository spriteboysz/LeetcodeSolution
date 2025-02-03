#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-16 22:48
FileName: P1089. 复写零
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                arr[i + 1: n] = arr[i: n - 1]
                i += 1
            i += 1
        ic(arr)


if __name__ == '__main__':
    Solution().duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0])
