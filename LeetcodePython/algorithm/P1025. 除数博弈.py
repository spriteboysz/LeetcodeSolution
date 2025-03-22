#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-22 21:37
FileName: algorithm/P1025. 除数博弈.py
Description: 
"""

from icecream import ic


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


if __name__ == '__main__':
    solution = Solution().divisorGame(2)
    ic(solution)
