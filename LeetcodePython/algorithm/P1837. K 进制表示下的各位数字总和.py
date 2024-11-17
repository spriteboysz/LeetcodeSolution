#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:31
FileName: P1837. K 进制表示下的各位数字总和
Description:
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n >= k:
            n, mod = divmod(n, k)
            total += mod
        return total + n


if __name__ == '__main__':
    solution = Solution().sumBase(34, 6)
    print(solution)
