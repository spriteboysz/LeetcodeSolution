#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 22:43
FileName: P0820. 单词的压缩编码
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len)
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i + 1:]):
                if word2.endswith(word1):
                    words[i] = ''
                    break
        return sum(len(word) + 1 for word in words if word != '')


if __name__ == '__main__':
    solution = Solution().minimumLengthEncoding(words=["time", "me", "bell"])
    ic(solution)
