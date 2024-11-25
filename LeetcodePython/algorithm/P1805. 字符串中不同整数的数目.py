#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:57
FileName: P1805. 字符串中不同整数的数目
Description:
"""
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        matches = re.findall(r'(\d+)', word)
        return len(set(map(int, matches)))


if __name__ == '__main__':
    solution = Solution().numDifferentIntegers(word="a123bc034d8ef34")
    print(solution)
