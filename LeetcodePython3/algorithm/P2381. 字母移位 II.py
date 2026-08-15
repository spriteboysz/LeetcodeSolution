#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 09:36
FileName: algorithm/P2381. 字母移位 II.py
Description: 
"""
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        moves = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            move = 1 if direction == 1 else - 1
            moves[start] += move
            moves[end + 1] -= move

        for i in range(1, len(s) + 1):
            moves[i] += moves[i - 1]
        ss = []
        for ch, move in zip(s, moves):
            ss.append(chr((ord(ch) + move - ord('a')) % 26 + ord('a')))
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]])
    print(solution)
