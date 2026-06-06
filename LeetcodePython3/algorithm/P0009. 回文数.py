#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 12:36
FileName: P0009. 回文数.py
Description:
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(121)
    print(solution)
