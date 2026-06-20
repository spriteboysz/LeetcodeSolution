#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:09
FileName: P1128. 等价多米诺骨牌对的数量.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(int)
        for domino in dominoes:
            dic[tuple(sorted(domino))] += 1
        return sum(v * (v - 1) // 2 for v in dic.values())


if __name__ == '__main__':
    solution = Solution().numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
    print(solution)
