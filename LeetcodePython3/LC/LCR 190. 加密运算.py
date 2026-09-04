#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:04
FileName: LC/LCR 190. 加密运算.py
Description: 
"""


class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        return sum([dataA, dataB])


if __name__ == '__main__':
    solution = Solution().encryptionCalculate(1, 2)
    print(solution)
