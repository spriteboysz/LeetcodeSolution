#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:10
FileName: P1925. 统计平方和三元组的数目.py
Description:
"""


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n):
            for b in range(1, n):
                c = int((a * a + b * b) ** 0.5)
                if a * a + b * b == c * c and c <= n:
                    cnt += 1

        return cnt


if __name__ == '__main__':
    solution = Solution().countTriples(10)
    print(solution)
