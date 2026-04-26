#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 19:38
FileName: P3913. 按频率对元音排序.py
Description:
"""

from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        count = defaultdict(int)
        index = defaultdict(lambda: len(s))
        for i, ch in enumerate(s):
            if ch not in 'aeiou':
                continue
            count[ch] += 1
            if index[ch] == len(s):
                index[ch] = i
        vowels = sorted(count, key=lambda el: (-count.get(el, 0), index.get(el)))
        ss = list(''.join(v * count.get(v, 0) for v in vowels))
        return ''.join(ss.pop(0) if ch in 'aeiou' else ch for i, ch in enumerate(s))


if __name__ == '__main__':
    solution = Solution().sortVowels(s="aeiaaioooa")
    print(solution)
