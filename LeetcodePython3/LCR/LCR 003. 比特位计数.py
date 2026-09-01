#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:20
FileName: LCR/LCR 003. 比特位计数.py
Description: 
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]


if __name__ == '__main__':
    solution = Solution().countBits(2)
    print(solution)
