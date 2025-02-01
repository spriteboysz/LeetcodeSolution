#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:53
FileName: P1592. 重新排列单词间的空格
Description:
"""

from icecream import ic


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.strip().split()
        cnt = len(text) - sum(map(len, words))
        if len(words) == 1:
            return words[0] + ' ' * cnt
        div, mod = divmod(cnt, len(words) - 1)
        return (' ' * div).join(words) + ' ' * mod


if __name__ == '__main__':
    solution = Solution().reorderSpaces(text="  this   is  a sentence ")
    ic(solution)
