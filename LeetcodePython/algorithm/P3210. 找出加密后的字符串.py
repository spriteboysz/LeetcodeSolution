#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:16
FileName: P3210. 找出加密后的字符串
Description:
"""


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]


if __name__ == '__main__':
    solution = Solution().getEncryptedString(s="dart", k=3)
    print(solution)
