#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:20
FileName: P1051. 高度检查器
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().heightChecker([1, 1, 4, 2, 1, 3])
    ic(solution)
