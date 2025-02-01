#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 10:23
FileName: P1688. 比赛中的配对次数
Description:
"""

from icecream import ic


class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            cnt += n // 2
            n = n // 2 + n % 2
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfMatches(7)
    ic(solution)
