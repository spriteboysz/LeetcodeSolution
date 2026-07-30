#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 21:24
FileName: P3986. 统计起止时间经过的秒数.py
Description:
"""


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def calc(tt):
            hh, mm, ss = map(int, tt.split(':'))
            return hh * 60 * 60 + mm * 60 + ss

        return calc(endTime) - calc(startTime)


if __name__ == '__main__':
    solution = Solution().secondsBetweenTimes(startTime="12:34:56", endTime="13:00:00")
    print(solution)
