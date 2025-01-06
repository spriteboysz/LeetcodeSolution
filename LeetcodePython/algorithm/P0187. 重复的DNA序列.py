#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 22:59
FileName: P0187. 重复的DNA序列
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i + 10]] += 1
        return [k for k, v in sequences.items() if v > 1]


if __name__ == '__main__':
    solution = Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    ic(solution)
