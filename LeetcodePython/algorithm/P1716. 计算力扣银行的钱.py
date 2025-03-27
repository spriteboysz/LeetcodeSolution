#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-27 22:19
FileName: algorithm/P1716. 计算力扣银行的钱.py
Description: 
"""

from icecream import ic


class Solution:
    def totalMoney(self, n: int) -> int:
        week, cnt = 1, 0
        for i in range(n):
            if i != 0 and i % 7 == 0:
                week += 1
            cnt += week + i % 7
        return cnt


if __name__ == '__main__':
    solution = Solution().totalMoney(20)
    ic(solution)
