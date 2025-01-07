#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:39
FileName: P2951. 找出峰值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i, num in enumerate(mountain[1:-1], start=1):
            if mountain[i - 1] < num and mountain[i + 1] < num:
                peaks.append(i)
        return peaks


if __name__ == '__main__':
    solution = Solution().findPeaks(mountain=[1, 4, 3, 8, 5])
    ic(solution)
