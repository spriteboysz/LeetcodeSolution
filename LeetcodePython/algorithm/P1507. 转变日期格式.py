#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-29 21:20
FileName: P1507. 转变日期格式
Description:
"""

from icecream import ic


class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dd, mm, yy = date.split()
        return f'{yy}-{int(months.index(mm) + 1):02d}-{int(dd[:-2]):02d}'


if __name__ == '__main__':
    solution = Solution().reformatDate("3th Oct 2052")
    ic(solution)
