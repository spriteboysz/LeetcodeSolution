#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 22:33
FileName: P2942. 查找包含给定字符的单词
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]


if __name__ == '__main__':
    solution = Solution().findWordsContaining(words=["leet", "code"], x="e")
    ic(solution)
