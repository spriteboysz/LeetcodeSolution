#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:04
FileName: P2108. 找出数组中的第一个回文字符串.py
Description:
"""
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''


if __name__ == '__main__':
    solution = Solution().firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"])
    print(solution)
