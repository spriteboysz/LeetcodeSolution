#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 19:37
FileName: P1009. 十进制整数的反码
Description:
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ss = [1 - int(ch) for ch in bin(n)[2:]]
        return int(''.join(map(str, ss)), 2)


if __name__ == '__main__':
    solution = Solution().bitwiseComplement(5)
    print(solution)
