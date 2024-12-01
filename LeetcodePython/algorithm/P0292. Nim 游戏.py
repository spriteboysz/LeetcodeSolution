#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 21:47
FileName: P0292. Nim 游戏
Description:
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == '__main__':
    solution = Solution().canWinNim(4)
    print(solution)
