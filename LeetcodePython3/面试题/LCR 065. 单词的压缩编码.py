#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:13
FileName: 面试题/LCR 065. 单词的压缩编码.py
Description: 
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len)
        for i, word1 in enumerate(words):
            for word2 in words[i + 1:]:
                if word2.endswith(word1):
                    words[i] = None
                    break
        return sum(len(word) + 1 for word in words if word)


if __name__ == '__main__':
    solution = Solution().minimumLengthEncoding(words=["time", "me", "bell"])
    print('<None>' if not solution else f'{solution=}')
