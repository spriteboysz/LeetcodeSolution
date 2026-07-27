#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 20:31
FileName: P3477. 水果成篮 II.py
Description:
"""
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        for fruit in fruits:
            for j, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[j] = -1
                    break
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numOfUnplacedFruits(fruits=[4, 2, 5], baskets=[3, 5, 4])
    print(solution)
