#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 15:50
FileName: algorithm/P0763. 划分字母区间.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i, c in enumerate(s):
            dic[c] = i
        partitions = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, dic[c])
            if end == i:
                partitions.append(end - start + 1)
                start = end + 1
        return partitions


if __name__ == '__main__':
    solution = Solution().partitionLabels('ababcbacadefegdehijhklij')
    print('<None>' if not solution else f'{solution=}')
