#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 09:29
FileName: algorithm/P0848. 字母移位.py
Description: 
"""
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        acc = 0
        for i in range(len(s) - 1, -1, -1):
            acc += shifts[i]
            shifts[i] = acc
        ss = []
        for ch, shift in zip(s, shifts):
            ss.append(chr(((ord(ch) + shift) - ord('a')) % 26 + ord('a')))
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().shiftingLetters(s="abc", shifts=[3, 5, 9])
    print(solution)
