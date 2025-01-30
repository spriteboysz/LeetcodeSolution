#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 21:48
FileName: P3042. 统计前后缀下标对 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for j, word2 in enumerate(words):
            for word1 in words[:j]:
                if word2.startswith(word1) and word2.endswith(word1):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"])
    ic(solution)
