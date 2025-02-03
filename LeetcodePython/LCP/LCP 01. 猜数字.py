#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 10:18
FileName: LCP 01. 猜数字
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(a == b for a, b in zip(guess, answer))


if __name__ == '__main__':
    solution = Solution().game(guess=[1, 2, 3], answer=[1, 2, 3])
    ic(solution)
