#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 12:00
FileName: P0720. 词典中最长的单词
Description:
"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda el: (-len(el), el))
        seen = set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in seen:
                    break
            else:
                return word
        return ''


if __name__ == '__main__':
    solution = Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
    print(solution)
