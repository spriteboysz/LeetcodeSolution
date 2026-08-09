#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:07
FileName: P3751. 范围内总波动值 I.py
Description:
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(num: int) -> int:
            if num <= 100:
                return 0
            s = str(num)
            return sum(s[i] > s[i - 1] and s[i] > s[i + 1] or s[i] < s[i - 1] and s[i] < s[i + 1]
                       for i in range(1, len(s) - 1))

        return sum(calc(i) for i in range(num1, num2 + 1))


if __name__ == '__main__':
    solution = Solution().totalWaviness(num1=120, num2=130)
    print(solution)
