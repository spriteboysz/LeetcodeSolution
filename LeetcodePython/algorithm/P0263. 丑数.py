#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 21:03
FileName: P0263. 丑数
Description:
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for num in [2, 3, 5]:
            while n % num == 0:
                n //= num
        return n == 1


if __name__ == '__main__':
    solution = Solution().isUgly(6)
    print(solution)
