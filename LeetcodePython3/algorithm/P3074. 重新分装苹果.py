#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 18:57
FileName: P3074. 重新分装苹果.py
Description:
"""
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total, acc = sum(apple), 0
        for i, c in enumerate(capacity):
            acc += c
            if acc >= total:
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2])
    print(solution)
