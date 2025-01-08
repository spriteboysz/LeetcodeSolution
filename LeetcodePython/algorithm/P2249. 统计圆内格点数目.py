#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-07 23:19
FileName: P2249. 统计圆内格点数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        seen = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (x - i) ** 2 + (y - j) ** 2 <= r * r:
                        seen.add((i, j))
        return len(seen)


if __name__ == '__main__':
    solution = Solution().countLatticePoints(circles=[[2, 2, 2], [3, 4, 1]])
    ic(solution)
