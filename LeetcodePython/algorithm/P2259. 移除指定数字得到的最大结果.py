#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-07 22:56
FileName: P2259. 移除指定数字得到的最大结果
Description:
"""

from icecream import ic


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = number.rfind(digit)
        if last == -1:
            return number
        for i, d in enumerate(number[:-1]):
            if d == digit and int(number[i + 1]) > int(d):
                return number[:i] + number[i + 1:]
        return number[:last] + number[last + 1:]


if __name__ == '__main__':
    solution = Solution().removeDigit(number="1231", digit="1")
    ic(solution)
