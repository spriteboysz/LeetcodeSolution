#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:50
FileName: P1805. 字符串中不同整数的数目.py
Description:
"""
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        matches = re.findall(r'(\d+)', word)
        return len(set(int(num) for num in matches))


if __name__ == '__main__':
    solution = Solution().numDifferentIntegers(word="a123bc34d8ef34")
    print(solution)
