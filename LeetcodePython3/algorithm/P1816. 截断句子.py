#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 19:52
FileName: P1816. 截断句子.py
Description:
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.strip().split()[:k])


if __name__ == '__main__':
    solution = Solution().truncateSentence(s="Hello how are you Contestant", k=4)
    print(solution)
