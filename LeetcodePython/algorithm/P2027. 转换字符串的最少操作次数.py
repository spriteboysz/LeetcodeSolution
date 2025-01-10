#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 21:25
FileName: P2027. 转换字符串的最少操作次数
Description:
"""

from icecream import ic


class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt, i = 0, 0
        while i < len(s):
            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumMoves("XXOX")
    ic(solution)
