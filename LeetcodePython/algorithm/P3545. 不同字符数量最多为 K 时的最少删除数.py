#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-24 09:58
FileName: algorithm/P3545. 不同字符数量最多为 K 时的最少删除数.py
Description: 
"""
from collections import defaultdict

from icecream import ic


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        return sum(sorted(dic.values(), reverse=True)[k:])


if __name__ == '__main__':
    solution = Solution().minDeletion(s="abc", k=2)
    ic(solution)
