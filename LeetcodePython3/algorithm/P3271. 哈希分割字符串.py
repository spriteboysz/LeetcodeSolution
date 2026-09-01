#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 08:52
FileName: algorithm/P3271. 哈希分割字符串.py
Description: 
"""


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ss = [s[i:i + k] for i in range(0, len(s), k)]
        for i, el in enumerate(ss):
            ss[i] = chr(sum(ord(ch) - ord('a') for ch in el) % 26 + ord('a'))
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().stringHash('abcd', 2)
    print(solution)
