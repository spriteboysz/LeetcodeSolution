#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-22 23:25
FileName: P1016. 子串能表示从 1 到 N 数字的二进制串.py
Description:
"""


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i + 1)[2:] in s for i in range(n))


if __name__ == '__main__':
    solution = Solution().queryString(s="0110", n=3)
    print(solution)
