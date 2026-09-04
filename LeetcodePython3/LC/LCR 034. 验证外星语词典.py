#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:22
FileName: LC/LCR 034. 验证外星语词典.py
Description: 
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        return sorted(words, key=lambda w: [dic[c] for c in w]) == words


if __name__ == '__main__':
    solution = Solution().isAlienSorted(
        words=["hello", "leetcode"],
        order="hlabcdefgijkmnopqrstuvwxyz"
    )
    print(solution)
