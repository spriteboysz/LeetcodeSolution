#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:26
FileName: P3206. 交替组 I.py
Description:
"""
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = colors + colors[:2]
        cnt = 0
        for i in range(2, len(colors)):
            if colors[i - 2] != colors[i - 1] and colors[i - 1] != colors[i]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 0, 1])
    print(solution)
