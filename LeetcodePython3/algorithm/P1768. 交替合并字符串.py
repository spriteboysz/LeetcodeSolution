#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 09:25
FileName: P1768. 交替合并字符串.py
Description:
"""
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(f'{ch1}{ch2}' for ch1, ch2 in zip_longest(word1, word2, fillvalue=''))


if __name__ == '__main__':
    solution = Solution().mergeAlternately(word1="abc", word2="pqr")
    print(solution)
