#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-25 22:58
FileName: 面试题 05.01. 插入
Description:
"""


class Solution:
    def insertBits(self, n: int, m: int, i: int, j: int) -> int:
        ss = list(bin(n)[2:].zfill(32))[::-1]
        mm = bin(m)[2:].zfill(j - i + 1)[::-1]
        ss[i:j+1] = list(mm)
        return int(''.join(ss[::-1]), 2)


if __name__ == '__main__':
    solution = Solution().insertBits(0, 31, 0, 4)
    print(solution)
