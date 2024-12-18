#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-17 22:51
FileName: P0168. Excel 表列名称
Description:
"""
from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ss, n = [], columnNumber
        while n:
            n, mod = divmod(n - 1, 26)
            ss.append(ascii_uppercase[mod])
        return ''.join(map(str, ss))[::-1]


if __name__ == '__main__':
    solution = Solution().convertToTitle(28)
    print(solution)
