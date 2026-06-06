#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:55
FileName: P0231. 2 的幂.py
Description:
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return bin(n).count('1') == 1


if __name__ == '__main__':
    solution = Solution().isPowerOfTwo(64)
    print(solution)
