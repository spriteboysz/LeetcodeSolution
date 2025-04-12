#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 11:43
FileName: algorithm/P3365. 重排子字符串以形成目标字符串.py
Description: 
"""

from icecream import ic


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        m = len(s) // k
        ss = [s[i:i + m] for i in range(0, len(s), m)]
        tt = [t[i:i + m] for i in range(0, len(s), m)]
        return sorted(ss) == sorted(tt)


if __name__ == '__main__':
    solution = Solution().isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3)
    ic(solution)
