#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 17:02
FileName: LC/LCR 120. 寻找文件副本.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        counter = Counter(documents)
        return [num for num, cnt in counter.items() if cnt > 1][0]


if __name__ == '__main__':
    solution = Solution().findRepeatDocument(documents=[2, 5, 3, 0, 5, 0])
    print(solution)
