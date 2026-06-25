#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:35
FileName: P1317. 将整数转换为两个无零整数的和.py
Description:
"""
from typing import List


class Solution:
    @staticmethod
    def check(num: int):
        return '0' not in str(num)

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            if self.check(a) and self.check(n - a):
                return [a, n - a]
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().getNoZeroIntegers(1000)
    print(solution)
