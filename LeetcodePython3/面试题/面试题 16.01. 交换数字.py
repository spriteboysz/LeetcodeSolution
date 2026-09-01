#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:01
FileName: 面试题/面试题 16.01. 交换数字.py
Description: 
"""
from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return numbers[::-1]


if __name__ == '__main__':
    solution = Solution().swapNumbers([1, 2])
    print(solution)
