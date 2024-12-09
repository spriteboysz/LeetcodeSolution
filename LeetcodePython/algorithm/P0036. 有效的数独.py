#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-09 22:50
FileName: P0036. 有效的数独
Description:
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums):
            nums = [int(num) for num in nums if num != '.']
            return len(nums) == len(set(nums)) and all([1 <= num <= 9 for num in nums])

        for row in board:
            if not check(row):
                return False
        for column in zip(*board):
            if not check(column):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = [board[i + x][j + y] for x in range(0, 3) for y in range(0, 3)]
                if not check(grid):
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().isValidSudoku(board=
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ])

    print(solution)
