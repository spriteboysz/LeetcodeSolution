#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:15
FileName: P2828. 判别首字母缩略词.py
Description:
"""
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(word[0] for word in words) == s


if __name__ == '__main__':
    solution = Solution().isAcronym(words=["alice", "bob", "charlie"], s="abc")
    print(solution)
