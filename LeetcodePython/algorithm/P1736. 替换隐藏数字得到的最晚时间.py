#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 21:52
FileName: P1736. 替换隐藏数字得到的最晚时间
Description:
"""

from icecream import ic


class Solution:
    def maximumTime(self, time: str) -> str:
        for i in range(24 * 60 - 1, -1, -1):
            hh, mm = divmod(i, 60)
            tt = f'{hh:02d}:{mm:02d}'
            for j in range(5):
                if time[j] != '?' and time[j] != tt[j]:
                    break
            else:
                return tt
        return 'Error'


if __name__ == '__main__':
    solution = Solution().maximumTime(time="2?:?0")
    ic(solution)
