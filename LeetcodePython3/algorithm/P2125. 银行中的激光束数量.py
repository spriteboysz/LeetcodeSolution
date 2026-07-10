#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:06
FileName: P2125. 银行中的激光束数量.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [v for row in bank if (v := row.count('1')) > 0]
        return sum(num1 * num2 for num1, num2 in pairwise(bank))


if __name__ == '__main__':
    solution = Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"])
    print(solution)
