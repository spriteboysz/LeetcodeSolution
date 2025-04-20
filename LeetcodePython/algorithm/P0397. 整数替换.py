#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 20:59
FileName: algorithm/P0397. 整数替换.py
Description: 
"""

from icecream import ic


class Solution:
    def integerReplacement(self, n: int) -> int:
        def dfs(cnt, cur):
            if cur == 1:
                return cnt
            if cur % 2 == 0:
                return dfs(cnt + 1, cur // 2)
            return min(dfs(cnt + 1, cur + 1), dfs(cnt + 1, cur - 1))

        return dfs(0, n)


if __name__ == '__main__':
    solution = Solution().integerReplacement(7)
    ic(solution)
