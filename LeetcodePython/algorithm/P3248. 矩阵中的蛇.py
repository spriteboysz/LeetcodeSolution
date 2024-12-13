#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:00
FileName: P3248. 矩阵中的蛇
Description:
"""
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        for command in commands:
            if command == 'DOWN':
                y += 1
            elif command == 'UP':
                y -= 1
            elif command == 'RIGHT':
                x += 1
            elif command == 'LEFT':
                x -= 1
            else:
                raise ValueError('Error')
        return x + y * n


if __name__ == '__main__':
    solution = Solution().finalPositionOfSnake(n=3, commands=["DOWN", "RIGHT", "UP"])
    print(solution)
