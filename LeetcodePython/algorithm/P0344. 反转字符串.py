#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 21:59
FileName: P0344. 反转字符串
Description:
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]


if __name__ == '__main__':
    Solution().reverseString(s=["h", "e", "l", "l", "o"])
