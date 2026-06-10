#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:24
FileName: P2586. 统计范围内的元音字符串数.py
Description:
"""
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(word[0] in 'aeiou' and word[-1] in 'aeiou' for word in words[left:right + 1])


if __name__ == '__main__':
    solution = Solution().vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4)
    print(solution)
