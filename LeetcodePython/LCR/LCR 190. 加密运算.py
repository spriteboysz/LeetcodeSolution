#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-03 21:26
FileName: LCR 190. 加密运算
Description:
"""


class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        return sum([dataA, dataB])


if __name__ == '__main__':
    solution = Solution().encryptionCalculate(5, -1)
    print(solution)
