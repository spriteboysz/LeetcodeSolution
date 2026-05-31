#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-31 15:22
FileName: P3945. 计算数字频率得分.py
Description:
"""
from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        counter = Counter(str(n))
        return sum(int(k) * v for k, v in counter.items())


if __name__ == '__main__':
    solution = Solution().digitFrequencyScore(122)
    print(solution)
