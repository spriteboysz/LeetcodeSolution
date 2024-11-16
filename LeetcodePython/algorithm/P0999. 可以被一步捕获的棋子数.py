#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:08
FileName: P0999. 可以被一步捕获的棋子数
Description:
"""
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt = 0
        for row in [*board, *zip(*board)]:
            ss = ''.join(row).replace('.', '')
            if 'pR' in ss:
                cnt += 1
            if 'Rp' in ss:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numRookCaptures([
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'p', '.', '.', '.', '.'],
        ['.', '.', '.', 'R', '.', '.', '.', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'p', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']])
    print(solution)
