#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-21 23:42
FileName: P0869. 重新排序得到 2 的幂.py
Description:
"""

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = Counter(str(n))
        return any(counter == Counter(str(2 ** i)) for i in range(32))


if __name__ == '__main__':
    solution = Solution().reorderedPowerOf2(65536)
    print(solution)
