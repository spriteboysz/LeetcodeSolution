#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 22:03
FileName: P3121. 统计特殊字母的数量 II.py
Description:
"""

from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = defaultdict(list)
        for i, c in enumerate(word):
            counter[c].append(i)
        return sum(c1 in counter and c2 in counter and counter.get(c1, [])[-1] < counter.get(c2, [])[0]
                   for c1, c2 in zip(ascii_lowercase, ascii_uppercase))


if __name__ == '__main__':
    solution = Solution().numberOfSpecialChars(word="aaAbcBC")
    print(solution)
