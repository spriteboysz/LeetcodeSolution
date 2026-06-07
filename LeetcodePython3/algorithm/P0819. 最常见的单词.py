#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:29
FileName: P0819. 最常见的单词.py
Description:
"""
import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'[^a-z]+', paragraph.lower())
        words = [word for word in words if word and word not in banned]
        counter = Counter(words)
        maximum = max(counter.values())
        for k, v in counter.items():
            if v == maximum:
                return k
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned=["hit"]
    )
    print(solution)
