#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:04
FileName: P0258. 各位相加
Description:
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(map(int, list(str(num))))
        return num


if __name__ == '__main__':
    solution = Solution().addDigits(38)
    print(solution)
