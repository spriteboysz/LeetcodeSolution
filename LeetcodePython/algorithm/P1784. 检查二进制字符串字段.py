#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 21:23
FileName: P1784. 检查二进制字符串字段
Description:
"""

from icecream import ic


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '0' not in s.strip('0')


if __name__ == '__main__':
    solution = Solution().checkOnesSegment("110")
    ic(solution)
