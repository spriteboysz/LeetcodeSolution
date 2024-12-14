#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:54
FileName: LCR 018. 验证回文串
Description:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [ch.lower() for ch in s if ch.isalnum()]
        return ss == ss[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
    print(solution)
