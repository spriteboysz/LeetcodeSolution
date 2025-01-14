#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 22:56
FileName: P2315. 统计星号
Description:
"""

from icecream import ic


class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt, cnt1 = 0, 0
        for ch in s:
            if ch == '|':
                cnt1 += 1
            if cnt1 % 2 == 0 and ch == '*':
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countAsterisks(s="l|*e*et|c**o|*de|")
    ic(solution)
