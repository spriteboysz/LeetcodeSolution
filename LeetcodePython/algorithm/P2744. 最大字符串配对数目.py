#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-04 12:55
FileName: P2744. 最大字符串配对数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        for j, word1 in enumerate(words):
            for _, word2 in enumerate(words[:j]):
                if word1[::-1] == word2:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"])
    ic(solution)
