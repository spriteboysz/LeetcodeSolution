#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:36
FileName: P0318. 最大单词长度乘积
Description:
"""
from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        values = []
        for word in words:
            value = reduce(lambda a, b: a | b, [2 ** (ord(ch) - ord('a')) for ch in word], 0)
            values.append(value)

        maximum = 0
        for i in range(len(words)):
            for j in range(i):
                if values[i] & values[j] == 0:
                    maximum = max(maximum, len(words[i]) * len(words[j]))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print(solution)
