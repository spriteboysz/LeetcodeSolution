#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 14:17
FileName: algorithm/P2259. 移除指定数字得到的最大结果.py
Description: 
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        if digit not in number:
            return number

        index = -1
        for i, d in enumerate(number):
            if d == digit:
                if i + 1 < len(number) and int(number[i + 1]) > int(d):
                    return number[:i] + number[i + 1:]
                index = i
        return number[:index] + number[index + 1:]


if __name__ == '__main__':
    solution = Solution().removeDigit(number="123", digit='3')
    print('<None>' if solution is None else f'{solution=}')
