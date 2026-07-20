#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 21:59
FileName: P0187. 重复的DNA序列.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = defaultdict(int)
        for i in range(10, len(s) + 1):
            dic[s[i - 10:i]] += 1
        return [k for k, v in dic.items() if v > 1]


if __name__ == '__main__':
    solution = Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(solution)
