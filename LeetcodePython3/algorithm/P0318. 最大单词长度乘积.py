#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 15:15
FileName: LC/P0318. 最大单词长度乘积.py
Description: 
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words))
        dic = dict()
        for word in words:
            value = 0
            for c in word:
                value |= 1 << (ord(c) - ord('a'))
                dic[word] = value

        products = []
        for i, word1 in enumerate(words):
            for word2 in words[:i]:
                if dic.get(word1, 0) & dic.get(word2, 0) == 0:
                    products.append(len(word1) * len(word2))
        return max(products, default=0)


if __name__ == '__main__':
    solution = Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print('<None>' if solution is None else f'{solution=}')
