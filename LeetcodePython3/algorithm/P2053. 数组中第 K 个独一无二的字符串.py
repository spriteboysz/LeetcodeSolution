#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:34
FileName: P2053. 数组中第 K 个独一无二的字符串.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        arr = [ch for ch in arr if counter.get(ch, 0) == 1]
        return arr[k - 1] if len(arr) >= k else ''


if __name__ == '__main__':
    solution = Solution().kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2)
    print(solution)
