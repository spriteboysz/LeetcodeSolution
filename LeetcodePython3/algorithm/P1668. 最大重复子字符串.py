#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 09:28
FileName: P1668. 最大重复子字符串.py
Description:
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(len(sequence) // len(word), -1, -1):
            if word * i in sequence:
                return i
        return 0


if __name__ == '__main__':
    solution = Solution().maxRepeating(sequence="ababc", word="ab")
    print(solution)
