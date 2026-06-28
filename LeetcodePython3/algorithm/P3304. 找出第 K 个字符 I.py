#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:32
FileName: P3304. 找出第 K 个字符 I.py
Description:
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        ss = 'a'
        while len(ss) < k:
            ss += ''.join(chr(ord('a') + (ord(ch) - ord('a') + 1) % 26) for ch in ss)
        return ss[k - 1]


if __name__ == '__main__':
    solution = Solution().kthCharacter(5)
    print(solution)
