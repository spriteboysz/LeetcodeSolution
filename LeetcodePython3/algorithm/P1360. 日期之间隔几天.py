#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 16:34
FileName: P1360. 日期之间隔几天.py
Description:
"""


class Solution:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def check(year: int):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @classmethod
    def calc(cls, date: str):
        yy, mm, dd = map(int, date.split('-'))
        days = 0
        for i in range(yy - 1971):
            days += 365 + int(cls.check(i + 1971))
        if cls.check(yy) and mm > 2:
            days += 1
        return days + sum(cls.months[:mm - 1]) + dd

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.calc(date2) - self.calc(date1))


if __name__ == '__main__':
    solution = Solution().daysBetweenDates(date1="2020-01-15", date2="2019-12-31")
    print(solution)
