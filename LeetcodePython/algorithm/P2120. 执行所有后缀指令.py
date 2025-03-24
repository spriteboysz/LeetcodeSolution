#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 18:23
FileName: algorithm/P2120. 执行所有后缀指令.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def calc(instructions):
            x, y = startPos
            for i, instruction in enumerate(instructions):
                if instruction == 'U':
                    x -= 1
                elif instruction == 'D':
                    x += 1
                elif instruction == 'R':
                    y += 1
                elif instruction == 'L':
                    y -= 1
                if x < 0 or y < 0 or x >= n or y >= n:
                    return i
            return len(instructions)

        return [calc(s[i:]) for i in range(len(s))]


if __name__ == '__main__':
    solution = Solution().executeInstructions(n=3, startPos=[0, 1], s="RRDDLU")
    ic(solution)
