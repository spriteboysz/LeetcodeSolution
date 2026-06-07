#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 12:14
FileName: P1154. 一年中的第几天.py
Description:
"""


class Solution:

    @classmethod
    def check(cls, year: int):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        yy, mm, dd = map(int, date.split('-'))
        if self.check(yy):
            months[1] = 29
        return sum(months[:mm - 1]) + dd


if __name__ == '__main__':
    solution = Solution().dayOfYear("2004-3-1")
    print(solution)
