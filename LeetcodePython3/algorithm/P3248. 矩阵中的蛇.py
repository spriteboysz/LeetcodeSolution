#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:42
FileName: P3248. 矩阵中的蛇.py
Description:
"""
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        for command in commands:
            if command == 'DOWN':
                x += 1
            if command == 'UP':
                x -= 1
            if command == 'LEFT':
                y -= 1
            if command == 'RIGHT':
                y += 1
        return x * n + y


if __name__ == '__main__':
    solution = Solution().finalPositionOfSnake(n=3, commands=["DOWN", "RIGHT", "UP"])
    print(solution)
