#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-09 23:07
FileName: algorithm/P2559. 统计范围内的元音字符串数.py
Description: 
"""
from itertools import accumulate
from typing import List

from icecream import ic


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = [word[0] in vowels and word[-1] in vowels for word in words]
        nums = [0, *accumulate(words)]
        return [nums[right + 1] - nums[left] for left, right in queries]


if __name__ == '__main__':
    solution = Solution().vowelStrings(words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]])
    ic(solution)
