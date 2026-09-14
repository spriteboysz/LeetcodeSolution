#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 15:27
FileName: LC/P2177. 找到和为给定整数的三个连续整数.py
Description: 
"""
from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        num //= 3
        return [num - 1, num, num + 1]


if __name__ == '__main__':
    solution = Solution().sumOfThree(33)
    print('<None>' if solution is None else f'{solution=}')
