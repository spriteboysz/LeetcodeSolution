#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:16
FileName: P2283. 判断一个数的数字计数是否等于数位的值.py
Description:
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(digit) for i, digit in enumerate(num))


if __name__ == '__main__':
    solution = Solution().digitCount(num="1210")
    print(solution)
