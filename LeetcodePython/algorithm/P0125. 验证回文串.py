#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 19:52
FileName: P0125. 验证回文串
Description:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [c.lower() for c in s if c.isalnum()]
        return ss == ss[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome("A man, a plan, a canal: Panama")
    print(solution)
    solution = Solution().isPalindrome("0P")
    print(solution)
