#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:19
FileName: P2710. 移除字符串中的尾随零.py
Description:
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


if __name__ == '__main__':
    solution = Solution().removeTrailingZeros(num="51230100")
    print(solution)
