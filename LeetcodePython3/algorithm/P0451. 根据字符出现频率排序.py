#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:39
FileName: P0451. 根据字符出现频率排序.py
Description:
"""
from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return ''.join(ch * counter.get(ch, 0) for ch in sorted(counter, key=lambda ch: -counter.get(ch, 0)))


if __name__ == '__main__':
    solution = Solution().frequencySort(s="tree")
    print(solution)
