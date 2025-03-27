#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-26 22:58
FileName: algorithm/P1668. 最大重复子字符串.py
Description: 
"""

from icecream import ic


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maximum = len(sequence) // len(word) + 1
        for i in range(maximum, 0, -1):
            if word * i in sequence:
                return i
        return 0


if __name__ == '__main__':
    solution = Solution().maxRepeating(sequence="ababc", word="ab")
    ic(solution)
