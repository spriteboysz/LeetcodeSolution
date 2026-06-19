#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 21:13
FileName: P1185. 一周中的第几天.py
Description:
"""


class Solution:
    @classmethod
    def check(cls, year: int):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = day
        for yy in range(1971, year):
            days += 365 + int(self.check(yy))
        days += sum(months[:month - 1]) + int(month > 2 and self.check(year))
        return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][(days + 4) % 7]


if __name__ == '__main__':
    solution = Solution().dayOfTheWeek(day=19, month=6, year=2026)
    print(solution)
