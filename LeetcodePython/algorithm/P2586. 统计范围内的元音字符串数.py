#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 11:47
FileName: P2586. 统计范围内的元音字符串数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(word[0] in vowels and word[-1] in vowels for word in words[left:right + 1])


if __name__ == '__main__':
    solution = Solution().vowelStrings(words=["are", "amy", "u"], left=0, right=2)
    ic(solution)
