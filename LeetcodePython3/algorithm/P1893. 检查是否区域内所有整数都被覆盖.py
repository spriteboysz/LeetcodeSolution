#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 23:15
FileName: P1893. 检查是否区域内所有整数都被覆盖.py
Description:
"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen = set(range(left, right + 1))
        for s, e in ranges:
            seen -= set(range(s, e + 1))
        return not seen


if __name__ == '__main__':
    solution = Solution().isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)
    print(solution)
