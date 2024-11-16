#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 20:16
FileName: P0342. 4的幂
Description:
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1


if __name__ == '__main__':
    solution = Solution().isPowerOfFour(64)
    print(solution)
