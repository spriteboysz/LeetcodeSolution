#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:23
FileName: LCR 069. 山脉数组的峰顶索引
Description:
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().peakIndexInMountainArray([1, 3, 5, 4, 2])
    print(solution)
