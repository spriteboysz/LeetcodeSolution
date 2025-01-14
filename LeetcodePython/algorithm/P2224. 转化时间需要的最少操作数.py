#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-13 23:18
FileName: P2224. 转化时间需要的最少操作数
Description:
"""

from icecream import ic


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hh1, mm1 = map(int, current.split(':'))
        hh2, mm2 = map(int, correct.split(':'))
        tt = hh2 * 60 - hh1 * 60 + mm2 - mm1
        cnt = 0
        for t in [60, 15, 5, 1]:
            div, tt = divmod(tt, t)
            cnt += div
        return cnt


if __name__ == '__main__':
    solution = Solution().convertTime(current="02:30", correct="04:35")
    ic(solution)
