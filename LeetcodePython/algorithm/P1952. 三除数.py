#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:26
FileName: P1952. 三除数
Description:
"""


class Solution:
    def isThree(self, n: int) -> bool:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        nums = {prime * prime for prime in primes}
        return n in nums


if __name__ == '__main__':
    solution = Solution().isThree(4)
    print(solution)
