#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:34
FileName: P3945. 计算数字频率得分.py
Description:
"""
from typing import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(num) * cnt for num, cnt in Counter(str(n)).items())


if __name__ == '__main__':
    solution = Solution().digitFrequencyScore(122)
    print(solution)
