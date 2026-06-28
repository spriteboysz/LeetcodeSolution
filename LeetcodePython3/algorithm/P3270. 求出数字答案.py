#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 19:53
FileName: P3270. 求出数字答案.py
Description:
"""


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ss = ''
        for ch1, ch2, ch3 in zip(f'{num1:04d}', f'{num2:04d}', f'{num3:04d}'):
            ss += min(ch1, ch2, ch3)
        return int(ss)


if __name__ == '__main__':
    solution = Solution().generateKey(1, 10, 1000)
    print(solution)
