#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-18 23:27
FileName: P1592. 重新排列单词间的空格.py
Description:
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.strip().split()
        n = len(text) - sum(len(word) for word in words)
        if len(words) == 1:
            div, mod = 0, n
        else:
            div, mod = divmod(n, len(words) - 1)
        return (' ' * div).join(words) + ' ' * mod


if __name__ == '__main__':
    solution = Solution().reorderSpaces(text=" practice   makes   perfect")
    print(solution)
