#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:33
FileName: P0338. 比特位计数.py
Description:
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [digit.bit_count() for digit in range(n + 1)]


if __name__ == '__main__':
    solution = Solution().countBits(5)
    print(solution)
