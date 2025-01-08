#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-07 23:27
FileName: P3114. 替换字符可以得到的最晚时间
Description:
"""

from icecream import ic


class Solution:
    def findLatestTime(self, s: str) -> str:
        for i in range(12 * 60 - 1, -1, -1):
            hh, mm = divmod(i, 60)
            t = f'{hh:02d}:{mm:02d}'
            for tt, ss in zip(t, s):
                if ss != '?' and tt != ss:
                    break
            else:
                return t
        return 'Error'


if __name__ == '__main__':
    solution = Solution().findLatestTime(s="0?:5?")
    ic(solution)
