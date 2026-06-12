#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:37
FileName: P2325. 解密消息.py
Description:
"""
from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        dic = {}
        lowercase = [ch for ch in ascii_lowercase]
        for ch in key:
            if ch == ' ' or ch in seen:
                continue
            dic[ch] = lowercase.pop(0)
            seen.add(ch)
        return ''.join(dic.get(ch, ' ') for ch in message)


if __name__ == '__main__':
    solution = Solution().decodeMessage(
        key="the quick brown fox jumps over the lazy dog",
        message="vkbs bs t suepuv"
    )
    print(solution)
