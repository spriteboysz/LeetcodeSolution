#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-19 23:14
FileName: P1374. 生成每种字符都是奇数个的字符串
Description:
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        return 'a' * n


if __name__ == '__main__':
    solution = Solution().generateTheString(4)
    print(solution)
