#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 22:05
FileName: P0507. 完美数.py
Description:
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        seen = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                seen.add(i)
                seen.add(num // i)
        return sum(seen) == num * 2


if __name__ == '__main__':
    solution = Solution().checkPerfectNumber(28)
    print(solution)
