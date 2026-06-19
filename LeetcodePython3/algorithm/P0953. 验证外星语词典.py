#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-18 23:20
FileName: P0953. 验证外星语词典.py
Description:
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {ch: i for i, ch in enumerate(order)}
        return sorted(words, key=lambda word: [dic.get(ch) for ch in word]) == words


if __name__ == '__main__':
    solution = Solution().isAlienSorted(
        words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"
    )
    print(solution)
