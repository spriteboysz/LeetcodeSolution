#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 22:48
FileName: P1323. 6 和 9 组成的最大数字.py
Description:
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        for i, digit in enumerate(digits):
            if digit == '6':
                digits[i] = '9'
                break
        return int(''.join(digits))


if __name__ == '__main__':
    solution = Solution().maximum69Number(9966)
    print(solution)
