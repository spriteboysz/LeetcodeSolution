#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 08:56
FileName: LC/LCP 01. 猜数字.py
Description: 
"""
from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(a == b for a, b in zip(guess, answer))


if __name__ == '__main__':
    solution = Solution().game([1, 2, 3], [1, 2, 3])
    print(solution)
