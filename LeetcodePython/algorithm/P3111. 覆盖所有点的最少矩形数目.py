#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 10:03
FileName: algorithm/P3111. 覆盖所有点的最少矩形数目.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        nums = sorted(set([x for x, _ in points]))
        cnt, cur = 0, -1
        for x in nums:
            if x > cur:
                cnt += 1
                cur = x + w
        return cnt


if __name__ == '__main__':
    solution = Solution().minRectanglesToCoverPoints([[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], 1)
    ic(solution)
