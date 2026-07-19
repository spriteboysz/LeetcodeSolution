#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:20
FileName: P0692. 前K个高频单词.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return sorted(counter, key=lambda w: (-counter.get(w, 0), w))[:k]


if __name__ == '__main__':
    solution = Solution().topKFrequent(
        words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        k=4
    )
    print(solution)
