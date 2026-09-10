#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 15:44
FileName: 面试题/面试题 16.11. 跳水板.py
Description: 
"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        return [longer * i + shorter * (k - i) for i in range(k + 1)]


if __name__ == '__main__':
    solution = Solution().divingBoard(1, 2, 3)
    print('<None>' if solution is None else f'{solution=}')
