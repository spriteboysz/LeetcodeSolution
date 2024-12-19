#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-19 22:55
FileName: P1408. 数组中的字符串匹配
Description:
"""
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len, reverse=True)
        return list({word2 for i, word1 in enumerate(words) for word2 in words[i + 1:] if word2 in word1})


if __name__ == '__main__':
    solution = Solution().stringMatching(words=["mass", "as", "hero", "superhero"])
    print(solution)
