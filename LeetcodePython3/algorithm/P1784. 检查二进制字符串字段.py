#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:07
FileName: P1784. 检查二进制字符串字段.py
Description:
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([ch for ch in s.split('0') if ch]) == 1


if __name__ == '__main__':
    solution = Solution().checkOnesSegment('1001')
    print(solution)
