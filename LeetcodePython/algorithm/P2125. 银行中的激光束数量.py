#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-08 22:10
FileName: P2125. 银行中的激光束数量
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [el.count('1') for el in bank if el.count('1') > 0]
        return sum(bank[i - 1] * bank[i] for i in range(1, len(bank)))


if __name__ == '__main__':
    solution = Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"])
    ic(solution)
