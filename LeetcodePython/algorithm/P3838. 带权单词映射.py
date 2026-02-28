#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-02-28 22:10
FileName: P3838. 带权单词映射.py
Description:
"""
from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join(chr(25 + 97 - sum(weights[ord(ch) - 97] for ch in word) % 26) for word in words)


if __name__ == '__main__':
    s = Solution().mapWordWeights(
        words=["abcd", "def", "xyz"],
        weights=[5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
    )
    print(s)
