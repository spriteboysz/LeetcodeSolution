#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-11 23:33
FileName: algorithm/P0916. 单词子集.py
Description: 
"""
from collections import defaultdict, Counter
from typing import List

from icecream import ic


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dic = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for k, v in count.items():
                dic[k] = max(dic[k], v)
        seen = []
        for word in words1:
            count = Counter(word)
            if all(count.get(k, 0) >= v for k, v in dic.items()):
                seen.append(word)
        return seen


if __name__ == '__main__':
    solution = Solution().wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["lc", "eo"]
    )
    ic(solution)
