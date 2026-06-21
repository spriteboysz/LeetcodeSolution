#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:28
FileName: P1929. 数组串联.py
Description:
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


if __name__ == '__main__':
    solution = Solution().getConcatenation([1, 2, 1])
    print(solution)
