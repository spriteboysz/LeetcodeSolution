#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:26
FileName: P2451. 差值数组不同的字符串.py
Description:
"""
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    @staticmethod
    def process(word):
        nums = []
        for ch1, ch2 in pairwise(word):
            nums.append(ord(ch1) - ord(ch2))
        return tuple(nums)

    def oddString(self, words: List[str]) -> str:
        dic = defaultdict(list)
        for word in words:
            dic[self.process(word)].append(word)
        for v in dic.values():
            if len(v) == 1:
                return v[0]
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().oddString(words=["dtzca", "dtzca", "dtzca", "yqyyo", "dtzca", "dtzca"])
    print(solution)
