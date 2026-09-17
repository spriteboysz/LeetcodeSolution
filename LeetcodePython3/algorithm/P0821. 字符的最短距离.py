#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 11:18
FileName: algorithm/P0821. 字符的最短距离.py
Description: 
"""
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        distances = [0 if ch == c else len(s) for ch in s]
        flag, curr = False, 0
        for i, distance in enumerate(distances):
            if distance == 0:
                flag = True
                curr = 0
            if flag:
                distances[i] = curr
                curr += 1

        flag, curr = False, 0
        for i in range(len(s) - 1, -1, -1):
            if distances[i] == 0:
                flag = True
                curr = 0
            if flag:
                distances[i] = min(curr, distances[i])
                curr += 1
        return distances


if __name__ == '__main__':
    solution = Solution().shortestToChar(s="loveleetcode", c="e")
    print('<None>' if solution is None else f'{solution=}')
