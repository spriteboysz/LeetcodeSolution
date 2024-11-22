#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 21:39
FileName: P3304. 找出第 K 个字符 I
Description:
"""
from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int) -> str:
        ss = ascii_lowercase + 'a'
        s = 'a'
        while len(s) <= k:
            s += ''.join([ss[ss.index(ch) + 1] for ch in s])
        print(s)
        return s[k - 1]


if __name__ == '__main__':
    solution = Solution().kthCharacter(5)
    print(solution)
