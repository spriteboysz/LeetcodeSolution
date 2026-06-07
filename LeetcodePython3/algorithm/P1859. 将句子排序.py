#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 19:54
FileName: P1859. 将句子排序.py
Description:
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words = sorted((int(word[-1]), word[:-1]) for word in s.strip().split())
        return ' '.join(word[1] for word in words)


if __name__ == '__main__':
    solution = Solution().sortSentence(s="is2 sentence4 This1 a3")
    print(solution)
