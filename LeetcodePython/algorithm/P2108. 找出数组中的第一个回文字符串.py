#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:33
FileName: P2108. 找出数组中的第一个回文字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''


if __name__ == '__main__':
    solution = Solution().firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"])
    ic(solution)
