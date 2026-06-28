#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 20:14
FileName: P3663. 出现频率最低的数字.py
Description:
"""
from typing import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = Counter(int(digit) for digit in str(n))
        return min(counter, key=lambda digit: (counter.get(digit, 0), digit))


if __name__ == '__main__':
    solution = Solution().getLeastFrequentDigit(723344511)
    print(solution)
