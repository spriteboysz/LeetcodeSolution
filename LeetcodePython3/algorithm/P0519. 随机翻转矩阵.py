#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:55
FileName: P0519. 随机翻转矩阵.py
Description:
"""
import random

from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.count = m * n - 1
        self.n_cols = n
        self.visited = set()

    def flip(self) -> List[int]:
        tmp = random.randint(0, self.count)
        while tmp in self.visited:
            tmp = random.randint(0, self.count)
        self.visited.add(tmp)
        return [tmp // self.n_cols, tmp % self.n_cols]

    def reset(self) -> None:
        self.visited.clear()


if __name__ == '__main__':
    solution = Solution(4, 5)
    print(solution)
