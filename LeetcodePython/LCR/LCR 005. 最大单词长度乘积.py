#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 20:39
FileName: LCR 005. 最大单词长度乘积
Description:
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = dict()
        for word in words:
            val = 0
            for ch in word:
                val |= 1 << (ord(ch) - ord('a'))
            dic[word] = val
        maximum = 0
        for i, word1 in enumerate(words):
            for word2 in words[:i]:
                if dic.get(word1) & dic.get(word2) == 0:
                    maximum = max(maximum, len(word1) * len(word2))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxProduct(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"])
    print(solution)
