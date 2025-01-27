#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:01
FileName: P2828. 判别首字母缩略词
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(word[0] for word in words) == s


if __name__ == '__main__':
    solution = Solution().isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy")
    ic(solution)
