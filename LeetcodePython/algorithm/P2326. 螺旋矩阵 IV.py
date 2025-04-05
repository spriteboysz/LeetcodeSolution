#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 11:43
FileName: algorithm/P2326. 螺旋矩阵 IV.py
Description: 
"""
from typing import Optional, List

from icecream import ic

from utils.node import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        matrix = [[-1] * n for _ in range(m)]
        i = j = di = 0
        while head:
            matrix[i][j] = head.val
            head = head.next
            dx, dy = directions[di]
            if not (0 <= i + dx < m and 0 <= j + dy < n and matrix[i + dx][j + dy] == -1):
                di = (di + 1) % 4
                dx, dy = directions[di]
            i += dx
            j += dy
        return matrix


if __name__ == '__main__':
    solution = Solution().spiralMatrix(3, 5, ListNode.create('[3,0,2,6,8,1,7,9,4,2,5,5,0]'))
    ic(solution)
