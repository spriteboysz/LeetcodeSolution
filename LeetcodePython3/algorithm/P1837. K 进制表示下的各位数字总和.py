#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 21:07
FileName: P1837. K 进制表示下的各位数字总和.py
Description:
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            n, mod = divmod(n, k)
            ans += mod
        return ans


if __name__ == '__main__':
    solution = Solution().sumBase(34, 6)
    print(solution)
