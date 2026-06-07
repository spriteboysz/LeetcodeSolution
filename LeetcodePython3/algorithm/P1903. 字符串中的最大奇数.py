#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:02
FileName: P1903. 字符串中的最大奇数.py
Description:
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ''


if __name__ == '__main__':
    solution = Solution().largestOddNumber(num="12345")
    print(solution)
