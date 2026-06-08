#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:58
FileName: P2114. 句子中的最多单词数.py
Description:
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)


if __name__ == '__main__':
    solution = Solution().mostWordsFound(sentences=["please wait", "continue to fight", "continue to win"])
    print(solution)
