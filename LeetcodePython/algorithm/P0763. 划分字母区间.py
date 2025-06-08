#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-28 22:25
FileName: algorithm/P0763. 划分字母区间.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        digits = [0] * 26
        for i, ch in enumerate(s):
            digits[ord(ch) - ord('a')] = i

        partition = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, digits[ord(ch) - ord('a')])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition


if __name__ == '__main__':
    solution = Solution().partitionLabels(s="ababcbacadefegdehijhklij")
    ic(solution)
