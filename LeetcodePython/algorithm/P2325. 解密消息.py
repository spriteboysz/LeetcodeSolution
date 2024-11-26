#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 22:40
FileName: P2325. 解密消息
Description:
"""
from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic, pos = {}, 0
        for ch in key:
            if ch == ' ' or ch in dic:
                continue
            dic[ch] = ascii_lowercase[pos]
            pos += 1
        return ''.join([dic.get(ch, ch) for ch in message])


if __name__ == '__main__':
    solution = Solution().decodeMessage(
        key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv")
    print(solution)
