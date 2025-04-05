#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 18:46
FileName: interview/面试题 16.11. 跳水板.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        minimum, maximum, diff = shorter * k, longer * k, longer - shorter
        return list(range(minimum, maximum + 1, diff))


if __name__ == '__main__':
    solution = Solution().divingBoard(1, 2, 3)
    ic(solution)
