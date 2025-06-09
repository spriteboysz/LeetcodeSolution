#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-09 22:41
FileName: algorithm/P1170. 比较字符串最小字母出现频次.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def func(s):
            alphabet = [0] * 26
            for ch in s:
                alphabet[ord(ch) - ord('a')] += 1
            return [c for c in alphabet if c != 0][0]

        words = sorted([func(word) for word in words], reverse=True)
        ans = []
        for query in queries:
            target = func(query)
            for i, num in enumerate(words):
                if target >= num:
                    ans.append(i)
                    break
        return ans


if __name__ == '__main__':
    solution = Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"])
    ic(solution)
