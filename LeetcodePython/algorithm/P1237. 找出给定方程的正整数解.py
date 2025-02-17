#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 17:37
FileName: P1237. 找出给定方程的正整数解
Description:
"""
from typing import List

from icecream import ic


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, function: 'CustomFunction', z: int) -> List[List[int]]:
        ans, x, y = [], 1, 1000
        while x <= 1000 and y >= 1:
            res = function.f(x, y)
            if res < z:
                x += 1
            elif res > z:
                y -= 1
            if res == z:
                ans.append([x, y])
                x += 1
                y -= 1
        return ans


if __name__ == '__main__':
    function = CustomFunction()
    solution = Solution().findSolution(function, 5)
    ic(solution)
