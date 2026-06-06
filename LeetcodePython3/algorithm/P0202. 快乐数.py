#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:17
FileName: P0202. 快乐数.py
Description:
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            if n == 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().isHappy(19)
    print(solution)
