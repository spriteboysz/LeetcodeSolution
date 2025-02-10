#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-09 21:43
FileName: 面试题 16.01. 交换数字
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return numbers[::-1]


if __name__ == '__main__':
    solution = Solution().swapNumbers([1, 2])
    ic(solution)
