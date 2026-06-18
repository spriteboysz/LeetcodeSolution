#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:55
FileName: P2942. 查找包含给定字符的单词.py
Description:
"""
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]


if __name__ == '__main__':
    solution = Solution().findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a")
    print(solution)
