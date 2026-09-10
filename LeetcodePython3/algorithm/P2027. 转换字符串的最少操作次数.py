#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:40
FileName: algorithm/P2027. 转换字符串的最少操作次数.py
Description: 
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        i = 0
        while True:
            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i += 1
            if i > len(s) - 1:
                break
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumMoves('XXOX')
    print('<None>' if solution is None else f'{solution=}')
