#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 21:40
FileName: P3754. 连接非零数字并乘以其数字和 I.py
Description:
"""


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(el) for el in str(n) if el != '0']
        if len(digits) == 0:
            return 0
        return int(''.join(map(str, digits))) * sum(digits)


if __name__ == '__main__':
    s = Solution().sumAndMultiply(n=10203004)
    print(s)
