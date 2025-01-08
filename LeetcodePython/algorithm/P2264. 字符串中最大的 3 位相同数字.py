#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 22:37
FileName: P2264. 字符串中最大的 3 位相同数字
Description:
"""

from icecream import ic


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if (s := str(i) * 3) in num:
                return s
        return ''


if __name__ == '__main__':
    solution = Solution().largestGoodInteger(num="2300019")
    ic(solution)
