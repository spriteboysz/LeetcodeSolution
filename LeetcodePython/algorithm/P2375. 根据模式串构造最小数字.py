#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 13:26
FileName: algorithm/P2375. 根据模式串构造最小数字.py
Description: 
"""
from string import digits
from icecream import ic


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        i, cur, n = 0, 1, len(pattern)
        ans = [''] * (n + 1)
        while i < n:
            if i and pattern[i] == 'I':
                i += 1
            while i < n and pattern[i] == 'I':
                ans[i] = digits[cur]
                cur += 1
                i += 1
            i0 = i
            while i < n and pattern[i] == 'D':
                i += 1
            for j in range(i, i0 - 1, -1):
                ans[j] = digits[cur]
                cur += 1
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution().smallestNumber(pattern="IIIDIDDD")
    ic(solution)
