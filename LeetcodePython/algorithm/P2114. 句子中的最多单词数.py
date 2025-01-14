#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 23:27
FileName: P2114. 句子中的最多单词数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.strip().split()) for sentence in sentences)


if __name__ == '__main__':
    solution = Solution().mostWordsFound(
        sentences=["alice and bob love leetcode",
                   "i think so too",
                   "this is great thanks very much"])
    ic(solution)
