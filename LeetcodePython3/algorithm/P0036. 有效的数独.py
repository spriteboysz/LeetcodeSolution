#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-05 22:05
FileName: P0036. 有效的数独.py
Description:
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums):
            nums = [num for num in nums if num != '.']
            return len(nums) == len(set(nums))

        if any(not check(row) for row in board):
            return False
        if any(not check(column) for column in zip(*board)):
            return False
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                grid = [board[i + dx][j + dy] for dx in range(3) for dy in range(3)]
                if not check(grid):
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().isValidSudoku(
        board=[
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
    )
    print(solution)
