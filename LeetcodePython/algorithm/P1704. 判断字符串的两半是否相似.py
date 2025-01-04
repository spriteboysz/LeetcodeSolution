#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:06
FileName: P1704. 判断字符串的两半是否相似
Description:
"""

from icecream import ic


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        m = len(s) // 2
        return sum(ch in vowels for ch in s[:m]) == sum(ch in vowels for ch in s[m:])


if __name__ == '__main__':
    solution = Solution().halvesAreAlike('book')
    ic(solution)
