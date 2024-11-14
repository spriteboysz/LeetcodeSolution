#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 22:49
FileName: P1360. 日期之间隔几天
Description:
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year):
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return year % 4 == 0

        def calc(date):
            month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            yy, mm, dd = map(int, date.split('-'))
            days = dd
            for year in range(1971, yy):
                days += 365 + int(is_leap_year(year))
            if is_leap_year(yy):
                month[2] = 29
            return days + sum(month[:mm])

        return abs(calc(date2) - calc(date1))


if __name__ == '__main__':
    solution = Solution().daysBetweenDates(date1="2020-01-15", date2="2019-12-31")
    print(solution)
