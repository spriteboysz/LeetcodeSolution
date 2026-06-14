#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:10
FileName: P1408. 数组中的字符串匹配.py
Description:
"""
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))
        matches = []
        for i, word1 in enumerate(words):
            for word2 in words[i + 1:]:
                if word1 in word2:
                    matches.append(word1)
                    break
        return matches


if __name__ == '__main__':
    solution = Solution().stringMatching(words=["mass", "as", "hero", "superhero"])
    print(solution)
