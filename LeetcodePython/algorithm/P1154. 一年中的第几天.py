#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 22:41
FileName: P1154. 一年中的第几天
Description:
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        def is_leap_year(year):
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return year % 4 == 0

        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        yy, mm, dd = map(int, date.split('-'))
        if is_leap_year(yy):
            month[2] += 1
        return sum(month[:mm]) + dd


if __name__ == '__main__':
    solution = Solution().dayOfYear('2019-2-10')
    print(solution)
