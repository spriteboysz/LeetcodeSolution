#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 14:48
FileName: LC/LCR 069. 山脉数组的峰顶索引.py
Description: 
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().peakIndexInMountainArray([0, 10, 5, 2])
    print('<None>' if not solution else f'{solution=}')
