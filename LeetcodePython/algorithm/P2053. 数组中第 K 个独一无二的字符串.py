#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-25 23:08
FileName: P2053. 数组中第 K 个独一无二的字符串
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        arr2 = [el for el in arr if counter.get(el) == 1]
        return '' if len(arr2) < k else arr2[k - 1]


if __name__ == '__main__':
    solution = Solution().kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2)
    print(solution)
