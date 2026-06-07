#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:10
FileName: P1704. 判断字符串的两半是否相似.py
Description:
"""


class Solution:
    @classmethod
    def calc(cls, word):
        return sum(ch.lower() in 'aeiou' for ch in word)

    def halvesAreAlike(self, s: str) -> bool:
        return self.calc(s[:len(s) // 2]) == self.calc(s[len(s) // 2:])


if __name__ == '__main__':
    solution = Solution().halvesAreAlike('book')
    print(solution)
