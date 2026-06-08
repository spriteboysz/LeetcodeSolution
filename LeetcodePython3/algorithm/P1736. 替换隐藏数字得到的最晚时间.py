#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:29
FileName: P1736. 替换隐藏数字得到的最晚时间.py
Description:
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        for i in range(24 * 60 - 1, -1, -1):
            hh, mm = divmod(i, 60)
            target = f'{hh:02d}:{mm:02d}'
            if all(t2 == '?' for t1, t2 in zip(target, time) if t1 != t2):
                return target
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().maximumTime(time="2?:?0")
    print(solution)
