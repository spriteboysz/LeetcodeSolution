#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 08:58
FileName: P1185. 一周中的第几天
Description
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap_year(year):
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return year % 4 == 0

        days = day + 3
        for y in range(1970, year):
            days += 365 + int(is_leap_year(y))
        if is_leap_year(year):
            months[2] += 1
        days += sum(months[:month])
        return weekday[days % 7]


if __name__ == '__main__':
    solution = Solution().dayOfTheWeek(day=31, month=8, year=2019)
    print(solution)
