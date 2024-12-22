#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 20:17
FileName: 面试题 01.04. 回文排列
Description:
"""

from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        return sum([v % 2 == 1 for k, v in counter.items()]) <= 1


if __name__ == '__main__':
    solution = Solution().canPermutePalindrome("tactcoa")
    print(solution)
