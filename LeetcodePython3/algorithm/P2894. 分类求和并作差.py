#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:17
FileName: P2894. 分类求和并作差.py
Description:
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for num in range(1, n + 1):
            if num % m != 0:
                num1 += num
            else:
                num2 += num
        return num1 - num2


if __name__ == '__main__':
    solution = Solution().differenceOfSums(10, 3)
    print(solution)
