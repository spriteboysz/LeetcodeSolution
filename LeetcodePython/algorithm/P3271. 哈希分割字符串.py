#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:21
FileName: P3271. 哈希分割字符串
Description:
"""

from icecream import ic


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ss = []
        for i in range(0, len(s), k):
            ss.append(chr(sum(ord(ch) - ord('a') for ch in s[i:i + k]) % 26 + ord('a')))
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().stringHash(s="abcd", k=2)
    ic(solution)
