#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 16:07
FileName: algorithm/P3545. 不同字符数量最多为 K 时的最少删除数.py
Description: 
"""
from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        return sum(sorted(counter.values(), reverse=True)[k:])


if __name__ == '__main__':
    solution = Solution().minDeletion(s="abc", k=2)
    print('<None>' if solution is None else f'{solution=}')
