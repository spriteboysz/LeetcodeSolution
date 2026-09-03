#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:47
FileName: LC/LCR 166. 珠宝的最高价值.py
Description: 
"""
from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        n, m = len(frame), len(frame[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    frame[i][j] += frame[i][j - 1]
                elif j == 0:
                    frame[i][j] += frame[i - 1][j]
                else:
                    frame[i][j] += max(frame[i][j - 1], frame[i - 1][j])
        return frame[-1][-1]


if __name__ == '__main__':
    solution = Solution().jewelleryValue(frame=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(solution)
