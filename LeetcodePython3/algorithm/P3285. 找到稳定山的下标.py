#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:11
FileName: P3285. 找到稳定山的下标.py
Description:
"""
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable = []
        for i, h in enumerate(height[1:], start=1):
            if height[i - 1] > threshold:
                stable.append(i)
        return stable


if __name__ == '__main__':
    solution = Solution().stableMountains(height=[1, 2, 3, 4, 5], threshold=2)
    print(solution)
