#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 09:17
FileName: P0748. 最短补全词.py
Description:
"""
from typing import List, Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter1 = Counter(ch for ch in licensePlate.lower() if ch.isalpha())
        words = sorted(words, key=len)
        for word in words:
            counter2 = Counter(word)
            if all(v <= counter2.get(k, 0) for k, v in counter1.items()):
                return word
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().shortestCompletingWord(
        licensePlate = "1s3 PSt",
        words = ["step", "steps", "stripe", "stepple"]
    )
    print(solution)
