#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:17
FileName: P3360. 移除石头游戏
Description:
"""

from icecream import ic


class Solution:
    def canAliceWin(self, n: int) -> bool:
        num, cnt = 10, 0
        while n >= num:
            n -= num
            num -= 1
            cnt += 1
        return cnt % 2 == 1


if __name__ == '__main__':
    solution = Solution().canAliceWin(12)
    ic(solution)
