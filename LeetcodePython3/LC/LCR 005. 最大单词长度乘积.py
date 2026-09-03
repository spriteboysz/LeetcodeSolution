#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:00
FileName: LC/LCR 005. 最大单词长度乘积.py
Description: 
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            v = 0
            for ch in word:
                v |= 1 << (ord(ch) - ord('a'))
            dic[word] = v

        cnt = 0
        for i, w1 in enumerate(words):
            for w2 in words[i + 1:]:
                if dic.get(w1, 0) & dic.get(w2, 0) == 0:
                    cnt = max(cnt, len(w1) * len(w2))
        return cnt


if __name__ == '__main__':
    solution = Solution().maxProduct(['abcw', 'baz', 'foo', 'bar', 'fxyz', 'abcdef'])
    print(solution)
