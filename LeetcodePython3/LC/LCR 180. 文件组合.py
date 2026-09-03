#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 00:22
FileName: LCR/LCR 180. 文件组合.py
Description: 
"""
from typing import List


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        combinations = []
        for start in range(1, target // 2 + 1):
            cnt = (2 * target - 2 * start + (2 * start + 1) ** 2 / 4) ** 0.5 - (2 * start + 1) / 2
            if cnt.is_integer():
                combinations.append(list(range(start, start + int(cnt) + 1)))
        return combinations


if __name__ == '__main__':
    solution = Solution().fileCombination(18)
    print(solution)
