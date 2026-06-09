#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 22:59
FileName: P2224. 转化时间需要的最少操作数.py
Description:
"""


class Solution:
    @staticmethod
    def calc(time):
        hh, mm = map(int, time.strip().split(':'))
        return hh * 60 + mm

    def convertTime(self, current: str, correct: str) -> int:
        diff = abs(self.calc(current) - self.calc(correct))
        cnt = 0
        for el in [60, 15, 5, 1]:
            div, diff = divmod(diff, el)
            cnt += div
        return cnt


if __name__ == '__main__':
    solution = Solution().convertTime(current="02:30", correct="04:35")
    print(solution)
