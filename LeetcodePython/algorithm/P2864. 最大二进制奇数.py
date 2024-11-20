#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:15
FileName: P2864. 最大二进制奇数
Description:
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt0, cnt1 = s.count('0'), s.count('1')
        return '1' * (cnt1 - 1) + '0' * cnt0 + '1'


if __name__ == '__main__':
    solution = Solution().maximumOddBinaryNumber('0101')
    print(solution)
