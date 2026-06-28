#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:43
FileName: P2595. 奇偶位数.py
Description:
"""
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        for i, ch in enumerate(bin(n)[2:][::-1]):
            if ch == '0':
                continue
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return [even, odd]


if __name__ == '__main__':
    solution = Solution().evenOddBit(50)
    print(solution)
