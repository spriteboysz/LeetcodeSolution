#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:59
FileName: P1507. 转变日期格式.py
Description:
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        dd, mm, yy = date.split()
        return f'{yy}-{months.index(mm):02d}-{int(dd[:-2]):02d}'


if __name__ == '__main__':
    solution = Solution().reformatDate(date="20th Oct 2052")
    print(solution)
