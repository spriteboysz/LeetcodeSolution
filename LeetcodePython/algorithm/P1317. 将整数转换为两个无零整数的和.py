#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 22:56
FileName: P1317. 将整数转换为两个无零整数的和
Description:
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(num):
            return '0' not in str(num)

        for i in range(1, n):
            if check(i) and check(n - i):
                return [i, n - i]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().getNoZeroIntegers(11)
    print(solution)
