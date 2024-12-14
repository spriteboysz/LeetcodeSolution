#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:20
FileName: P3206. 交替组 I
Description:
"""
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = colors + colors[:2]
        cnt = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i + 1] and colors[i - 1] != colors[i]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 0, 1])
    print(solution)
