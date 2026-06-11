#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:54
FileName: P3114. 替换字符可以得到的最晚时间.py
Description:
"""


class Solution:
    def findLatestTime(self, s: str) -> str:
        for i in range(12 * 60 - 1, -1, -1):
            hh, mm = divmod(i, 60)
            curr = f'{hh:02d}:{mm:02d}'
            if all(ch2 == '?' for ch1, ch2 in zip(curr, s) if ch1 != ch2):
                return curr
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().findLatestTime(s="1?:?4")
    print(solution)
