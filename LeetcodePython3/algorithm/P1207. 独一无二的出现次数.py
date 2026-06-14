#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:14
FileName: P1207. 独一无二的出现次数.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr).values()
        return len(counter) == len(set(counter))


if __name__ == '__main__':
    solution = Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])
    print(solution)
