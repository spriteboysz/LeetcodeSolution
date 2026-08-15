#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 21:18
FileName: algorithm/P1338. 数组大小减半.py
Description: 
"""
from typing import List, Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        keys = sorted(counter, key=lambda el: counter.get(el, 0), reverse=True)
        acc = 0
        for i, key in enumerate(keys):
            acc += counter[key]
            if acc >= len(arr) // 2:
                return i + 1
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    print(solution)
