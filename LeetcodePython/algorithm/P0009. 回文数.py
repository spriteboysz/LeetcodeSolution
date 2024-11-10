#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 09:39
FileName: P0009. 回文数
Description:
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution().isPalindrome(x=121)
    print(s)
