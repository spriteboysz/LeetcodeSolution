#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 16:16
FileName: algorithm/P0748. 最短补全词.py
Description: 
"""
from typing import List
from collections import defaultdict, Counter

from icecream import ic


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dic = defaultdict(int)
        for c in licensePlate:
            if not c.isalpha():
                continue
            dic[c.lower()] += 1
        words.sort(key=len)
        for word in words:
            counter = Counter(word)
            if all(counter[k] >= v for k, v in dic.items()):
                return word
        return ''


if __name__ == '__main__':
    solution = Solution().shortestCompletingWord(
        licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"])
    ic(solution)
