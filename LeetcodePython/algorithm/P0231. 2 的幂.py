#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 22:57
FileName: P0231. 2 的幂
Description:
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n.bit_count() == 1


if __name__ == '__main__':
    solution = Solution().isPowerOfTwo(1)
    print(solution)
