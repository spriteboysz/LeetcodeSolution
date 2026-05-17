#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-03 15:59
FileName: P3227. 字符串元音游戏.py
Description:
"""


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(ch in 'aeiou' for ch in s)


if __name__ == '__main__':
    solution = Solution().doesAliceWin(s="leetcoder")
    print(solution)
