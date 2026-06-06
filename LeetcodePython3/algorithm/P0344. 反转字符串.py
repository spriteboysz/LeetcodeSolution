#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:35
FileName: P0344. 反转字符串.py
Description:
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        print(s)


if __name__ == '__main__':
    Solution().reverseString(s=["h", "e", "l", "l", "o"])
    # print(solution)
