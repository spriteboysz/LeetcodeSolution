#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 22:51
FileName: P2951. 找出峰值.py
Description:
"""
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i, num in enumerate(mountain[1:-1], start=1):
            if num > mountain[i - 1] and num > mountain[i + 1]:
                peaks.append(i)
        return peaks


if __name__ == '__main__':
    solution = Solution().findPeaks([1, 4, 3, 8, 5])
    print(solution)
