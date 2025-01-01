#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:01
FileName: LCR 065. 单词的压缩编码
Description:
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len)
        total = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i + 1:]):
                if word2.endswith(word1):
                    break
            else:
                total += len(word1) + 1
        return total


if __name__ == '__main__':
    solution = Solution().minimumLengthEncoding(["time", "me", "bell"])
    print(solution)
