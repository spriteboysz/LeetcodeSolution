#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:24
FileName: P0292. Nim 游戏.py
Description:
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == '__main__':
    solution = Solution().canWinNim(4)
    print(solution)
