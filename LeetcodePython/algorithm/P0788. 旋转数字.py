#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-24 22:43
FileName: P0788. 旋转数字
Description:
"""

from icecream import ic


class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(num):
            for digit in {'3', '4', '7'}:
                if digit in str(num):
                    return False
            for digit in {'2', '5', '6', '9'}:
                if digit in str(num):
                    return True
            return False

        return sum(check(str(i)) for i in range(n + 1))


if __name__ == '__main__':
    solution = Solution().rotatedDigits(10)
    ic(solution)
